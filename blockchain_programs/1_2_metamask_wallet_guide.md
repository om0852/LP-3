# Assignments 1 and 2: MetaMask installation, wallet creation and Ether spent per transaction

## Aim

1. Install MetaMask and study how much Ether is spent per transaction.
2. Create your own wallet using MetaMask for crypto transactions.

## Theory

- **MetaMask** is a browser extension (and mobile app) that works as a crypto wallet
  and as a gateway to Ethereum-compatible blockchains. It stores your private keys
  locally and signs transactions for you.
- **Wallet**: a pair of keys. The *public address* (for example `0x71C7...976F`) is
  shared to receive funds. The *private key* proves ownership and must never be shared.
- **Secret Recovery Phrase**: 12 words from which all the accounts of the wallet can be
  regenerated. Anyone who has it controls the wallet.
- **Gas**: the unit that measures the computation a transaction needs.
  A plain Ether transfer always needs **21,000 gas**.
- **Transaction fee** (after EIP-1559):

  ```
  fee = gas used x (base fee + priority fee)
  ```

  The base fee is burned, the priority fee (tip) goes to the validator.
  Gas prices are quoted in **gwei** (1 gwei = 10^-9 ETH).

## Part A: Install MetaMask

1. Open <https://metamask.io/download> in Chrome, Firefox, Brave or Edge.
2. Click **Install MetaMask** and add the extension from the browser's official store.
3. Pin the fox icon to the toolbar so it is easy to reach.

## Part B: Create the wallet

1. Click the MetaMask icon and choose **Create a new wallet**.
2. Accept or decline the usage-data prompt, then set a strong password.
   The password only unlocks MetaMask on this device.
3. Choose **Secure my wallet**. MetaMask shows the 12-word Secret Recovery Phrase.
4. Write the phrase on paper and store it offline. Do not screenshot it or save it in the cloud.
5. Confirm the phrase by selecting the missing words in order.
6. The wallet is ready. **Account 1** and its address appear at the top; click the address to copy it.

## Part C: Connect to a test network and get test Ether

Test networks use Ether that has no real value, so experiments cost nothing.

1. Open the network menu (top left) and switch on **Show test networks**.
2. Select **Sepolia**.
3. Copy your address and request test Ether from a Sepolia faucet
   (search for "Sepolia faucet"; several are free and some need a sign-in).
4. Wait for the balance to appear in MetaMask.

## Part D: Send a transaction and study the Ether spent

1. Create a second account: account menu, then **Add account**.
2. From Account 1 click **Send**, paste the address of Account 2 and enter an amount, for example `0.01` SepoliaETH.
3. On the confirmation screen note the **estimated gas fee** and the **total** (amount + fee).
4. Click **Confirm**. When the transaction is confirmed, open it in the **Activity** tab
   and choose **View on block explorer** (Sepolia Etherscan).
5. Record the values below.

| Field | Meaning | Observed value |
|-------|---------|----------------|
| Transaction hash | Unique ID of the transaction | |
| Block number | Block that included it | |
| From / To | Sender and receiver addresses | |
| Value | Ether transferred | |
| Gas limit | Maximum gas the sender allowed | |
| Gas used | Gas actually consumed (21,000 for a transfer) | |
| Base fee (gwei) | Network fee per gas, burned | |
| Priority fee (gwei) | Tip per gas, paid to the validator | |
| Transaction fee (ETH) | Gas used x (base + priority) | |

### Worked example

With gas used = 21,000, base fee = 20 gwei and priority fee = 1.5 gwei:

```
fee = 21,000 x (20 + 1.5) gwei
    = 451,500 gwei
    = 0.0004515 ETH
```

If 0.01 ETH is sent, Account 1 loses 0.01 + 0.0004515 = 0.0104515 ETH and
Account 2 gains exactly 0.01 ETH.

## Observations

- The sender always pays the fee; the receiver gets the full value.
- A plain transfer uses exactly 21,000 gas. Contract calls use more because they run code.
- The fee depends on network demand: a busier network means a higher base fee.
- A higher priority fee gets the transaction confirmed sooner.
- A failed transaction still costs gas, because validators did the work.

## Conclusion

MetaMask was installed, a wallet was created and secured with a recovery phrase,
test Ether was received on the Sepolia network, and a transfer was made.
The Ether spent on a transaction equals the gas used multiplied by the gas price.
