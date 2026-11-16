/* global getAssetRegistry getFactory emit query */
'use strict';

/**
 * Transfer a commodity from its current owner to a new owner.
 * @param {org.example.trading.Trade} trade - the trade to be processed
 * @transaction
 */
async function tradeCommodity(trade) {
    const oldOwner = trade.commodity.owner;

    if (oldOwner.getIdentifier() === trade.newOwner.getIdentifier()) {
        throw new Error('The new owner already owns this commodity');
    }

    // Change the owner and save the asset
    trade.commodity.owner = trade.newOwner;
    const assetRegistry = await getAssetRegistry('org.example.trading.Commodity');
    await assetRegistry.update(trade.commodity);

    // Tell listening applications about the trade
    const notification = getFactory().newEvent('org.example.trading', 'TradeNotification');
    notification.commodity = trade.commodity;
    notification.oldOwner = oldOwner;
    notification.newOwner = trade.newOwner;
    emit(notification);
}

/**
 * Remove all commodities whose quantity is above 60.
 * @param {org.example.trading.RemoveHighQuantityCommodities} remove - the remove request
 * @transaction
 */
async function removeHighQuantityCommodities(remove) { // eslint-disable-line no-unused-vars
    const assetRegistry = await getAssetRegistry('org.example.trading.Commodity');
    const results = await query('selectCommoditiesWithHighQuantity');

    for (const commodity of results) {
        const notification = getFactory().newEvent('org.example.trading', 'RemoveNotification');
        notification.commodity = commodity;
        emit(notification);
        await assetRegistry.remove(commodity);
    }
}
