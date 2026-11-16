# Assignment 6: Business network using Hyperledger

A small **commodity trading network** written for Hyperledger Composer,
the tool that models a business network on top of Hyperledger Fabric.

> Hyperledger Composer was deprecated in 2019. It still works for learning and is
> what this assignment is normally done with. New production projects write
> Fabric chaincode directly.

## Files

| File | Purpose |
|------|---------|
| `models/org.example.trading.cto` | Model: participants, assets, transactions and events |
| `lib/logic.js` | Transaction processor functions (the business logic) |
| `permissions.acl` | Access-control rules |
| `queries.qry` | Named queries |
| `package.json` | Name and version of the business network |

## The network

- **Participant**: `Trader` (trader ID, first name, last name)
- **Asset**: `Commodity` (trading symbol, description, quantity, owner)
- **Transaction**: `Trade` moves a commodity to a new owner
- **Transaction**: `RemoveHighQuantityCommodities` deletes commodities with quantity above 60
- **Event**: `TradeNotification` is emitted after every trade

## Option A: Composer Playground (no installation)

1. Open Composer Playground (online, or locally with `composer-playground`).
2. Choose **Deploy a new business network**, then **empty-business-network**.
3. Replace the model file, script file, ACL file and query file with the files in this folder.
4. Click **Deploy changes**.
5. Open the **Test** tab:
   - Create two `Trader` participants, for example `TRADER1` and `TRADER2`.
   - Create a `Commodity` with owner `resource:org.example.trading.Trader#TRADER1`.
   - Submit a `Trade` transaction with the commodity and `TRADER2` as the new owner.
6. Check that the owner of the commodity changed and that the transaction appears
   in **All Transactions** (the historian).

## Option B: Local Fabric with the Composer CLI

Needs Node.js 8, Docker and the Fabric development servers from the Composer documentation.

```bash
npm install -g composer-cli@0.20
```

```bash
composer archive create -t dir -n .
```

```bash
composer network install --card PeerAdmin@hlfv1 --archiveFile trading-network@0.0.1.bna
```

```bash
composer network start --networkName trading-network --networkVersion 0.0.1 --networkAdmin admin --networkAdminEnrollSecret adminpw --card PeerAdmin@hlfv1 --file networkadmin.card
```

```bash
composer card import --file networkadmin.card
```

```bash
composer network ping --card admin@trading-network
```

```bash
composer-rest-server -c admin@trading-network -n never
```

The last command starts a REST API at <http://localhost:3000/explorer> for the network.

## Sample test data

Trader:

```json
{
  "$class": "org.example.trading.Trader",
  "tradeId": "TRADER1",
  "firstName": "Asha",
  "lastName": "Patil"
}
```

Commodity:

```json
{
  "$class": "org.example.trading.Commodity",
  "tradingSymbol": "GOLD",
  "description": "Gold bars",
  "mainExchange": "MCX",
  "quantity": 50,
  "owner": "resource:org.example.trading.Trader#TRADER1"
}
```

Trade:

```json
{
  "$class": "org.example.trading.Trade",
  "commodity": "resource:org.example.trading.Commodity#GOLD",
  "newOwner": "resource:org.example.trading.Trader#TRADER2"
}
```
