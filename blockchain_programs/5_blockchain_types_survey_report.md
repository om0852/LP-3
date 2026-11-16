# Assignment 5: Survey report on types of blockchains and their real-time use cases

## 1. Introduction

A blockchain is a distributed ledger in which records (transactions) are grouped into
blocks, and each block stores the cryptographic hash of the previous one. Changing an
old record would change its hash and break every later link, so the history is
tamper-evident. Copies of the ledger are held by many nodes, and a consensus mechanism
decides which new block is accepted.

Blockchains differ mainly in two questions:

- **Who may join and read the ledger?** (public or private)
- **Who may validate transactions?** (permissionless or permissioned)

The answers give four commonly recognised types: public, private, consortium and hybrid.

## 2. Types of blockchains

### 2.1 Public blockchain

Anyone can join, read the ledger, send transactions and take part in consensus.
No central authority exists.

- **Consensus**: Proof of Work (Bitcoin), Proof of Stake (Ethereum, Cardano, Solana).
- **Advantages**: fully decentralised, transparent, censorship-resistant, very hard to tamper with.
- **Limitations**: lower throughput, transaction fees that rise with demand,
  all data is visible to everyone, Proof of Work consumes a lot of energy.
- **Examples**: Bitcoin, Ethereum, Litecoin, Solana.

### 2.2 Private blockchain

A single organisation controls who can join and who can validate.
It keeps the data structure of a blockchain but is run centrally.

- **Consensus**: Raft, Practical Byzantine Fault Tolerance (PBFT), Proof of Authority.
- **Advantages**: high speed, low cost, data privacy, easy to govern and upgrade.
- **Limitations**: centralised trust, fewer nodes so weaker tamper resistance,
  participants must trust the operator.
- **Examples**: Hyperledger Fabric (single-organisation deployment), Corda, Quorum.

### 2.3 Consortium (federated) blockchain

A group of organisations shares control. Only pre-approved nodes validate,
and no single member owns the network.

- **Consensus**: PBFT, Raft, Istanbul BFT, voting-based schemes.
- **Advantages**: shared governance, better performance than public chains,
  privacy between members, suited to cooperation between competitors.
- **Limitations**: setting up governance between organisations is slow,
  the network is only as trustworthy as its members, some risk of collusion.
- **Examples**: R3 Corda networks, Energy Web Chain, Hyperledger Fabric multi-organisation networks.

### 2.4 Hybrid blockchain

Combines a private, permissioned part with a public part. The organisation decides
which data stays private and which is published or anchored on a public chain for proof.

- **Advantages**: confidential data stays private while proofs remain publicly verifiable;
  flexible access rules.
- **Limitations**: more complex design, transparency depends on what the owner chooses to publish.
- **Examples**: XDC Network, Dragonchain.

## 3. Comparison

| Feature | Public | Private | Consortium | Hybrid |
|---------|--------|---------|------------|--------|
| Access | Anyone | One organisation | Selected organisations | Mixed |
| Permission to validate | Permissionless | Permissioned | Permissioned | Permissioned, with public parts |
| Decentralisation | High | Low | Medium | Medium |
| Speed | Low to medium | High | High | High |
| Transaction cost | Variable, can be high | Low | Low | Low |
| Data privacy | Low | High | High among members | Configurable |
| Typical consensus | PoW, PoS | Raft, PoA | PBFT, Raft | Mixed |
| Examples | Bitcoin, Ethereum | Fabric, Quorum | Corda, Energy Web | XDC, Dragonchain |

## 4. Real-time use cases

### 4.1 Finance and payments

- **Cryptocurrencies** (public): Bitcoin and Ether move value between people without a bank.
- **Cross-border payments**: blockchain settlement reduces the days taken by
  correspondent banking to minutes. Stablecoins such as USDC are used for remittances.
- **Decentralised finance (DeFi)** (public): lending, borrowing and trading run by
  smart contracts on Ethereum, for example Aave and Uniswap.
- **Central bank digital currencies**: several central banks have piloted or launched
  digital currencies on permissioned ledgers, for example India's Digital Rupee pilot
  and China's e-CNY.

### 4.2 Supply chain and logistics

- **Food traceability** (consortium): IBM Food Trust, used by Walmart, traces produce
  from farm to shelf in seconds instead of days, which speeds up recalls.
- **Provenance of high-value goods**: De Beers' Tracr tracks diamonds from mine to
  retailer to prove they are conflict-free.
- **Pharmaceuticals**: tracking medicine batches helps detect counterfeit drugs.

### 4.3 Healthcare

- Sharing patient records between hospitals with patient-controlled access.
- Recording clinical-trial data so that results cannot be altered afterwards.
- Verifying the credentials of medical staff.

### 4.4 Government and public services

- **Land records**: several governments, including some Indian states, have piloted
  land registries on blockchain to reduce fraud and title disputes.
- **Digital identity**: Estonia secures many of its e-government records with
  blockchain-style integrity proofs (KSI).
- **Certificates**: universities issue degree certificates that employers can verify
  instantly.

### 4.5 Energy

- Peer-to-peer energy trading, where households with solar panels sell surplus power
  to neighbours (for example Power Ledger).
- Tracking renewable-energy certificates on the Energy Web Chain.

### 4.6 Digital assets and media

- **Non-fungible tokens (NFTs)** record ownership of digital art, tickets and game items.
- **Tokenisation** of real-world assets such as property, bonds and funds.
- Royalty tracking for music and digital content.

### 4.7 Other areas

- **Insurance**: parametric policies that pay out automatically, for example on a
  verified flight delay.
- **Internet of Things**: devices record sensor data on a ledger for audit.
- **Voting**: pilot projects use blockchains to make vote counts verifiable.

## 5. Choosing a type

| Requirement | Suitable type |
|-------------|---------------|
| Open participation, no trusted party | Public |
| Internal records of one company, high speed | Private |
| Several organisations sharing data and control | Consortium |
| Private data with public proof | Hybrid |

## 6. Challenges

- **Scalability**: public chains process far fewer transactions per second than card networks;
  layer-2 networks and sharding address this.
- **Interoperability**: different chains do not communicate easily.
- **Regulation**: rules for crypto assets differ between countries and keep changing.
- **Privacy versus transparency**: public data conflicts with data-protection laws.
- **Energy use**: a concern for Proof of Work; Proof of Stake uses far less energy.
- **Key management**: a lost private key means lost access.

## 7. Conclusion

No single type of blockchain suits every problem. Public blockchains give the strongest
decentralisation and are used for cryptocurrencies and open financial applications.
Private and consortium blockchains trade some decentralisation for speed, privacy and
control, which suits enterprises and groups of organisations. Hybrid blockchains combine
both. Real deployments in payments, supply chains, healthcare, government records and
energy show that the choice depends on who must be trusted, who may see the data and
how fast the system must be.

## References

1. S. Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System", 2008.
2. V. Buterin, "Ethereum White Paper", 2014.
3. Hyperledger Fabric documentation, <https://hyperledger-fabric.readthedocs.io>
4. Ethereum documentation, <https://ethereum.org/en/developers/docs>
5. I. Bashir, "Mastering Blockchain", Packt Publishing.
