// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/*
 * Assignment 3: Smart contract for the bank account of a customer.
 * Operations: deposit money, withdraw money, show balance.
 *
 * How to run (Remix + test network):
 *   1. Open https://remix.ethereum.org and paste this file.
 *   2. Compile with Solidity 0.8.20 or newer.
 *   3. Deploy with "Remix VM" for a quick test, or choose
 *      "Injected Provider - MetaMask" on the Sepolia test network.
 *   4. deposit    : enter an amount in the VALUE box, then click deposit.
 *      withdraw   : enter the amount in wei, then click withdraw.
 *      showBalance: click to read your balance (free, no gas).
 */
contract Bank {
    // Each customer (address) has their own balance, stored in wei.
    mapping(address => uint256) private balances;

    event Deposited(address indexed customer, uint256 amount);
    event Withdrawn(address indexed customer, uint256 amount);

    // Deposit money: the Ether sent with the call is added to the caller's balance.
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    // Withdraw money: sends `amount` wei back to the caller.
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the balance before sending Ether (prevents re-entrancy).
        balances[msg.sender] -= amount;

        (bool sent, ) = payable(msg.sender).call{value: amount}("");
        require(sent, "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Show balance of the caller, in wei.
    function showBalance() external view returns (uint256) {
        return balances[msg.sender];
    }
}
