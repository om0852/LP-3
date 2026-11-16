// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/*
 * Assignment 4: Student data using structures, arrays and a fallback function.
 *
 * How to run:
 *   1. Open https://remix.ethereum.org, paste this file and compile (0.8.20+).
 *   2. Deploy on "Remix VM" or on Sepolia through MetaMask.
 *   3. Call addStudent(1, "Asha", "Computer", 85) and the getter functions.
 *   4. To trigger the fallback: in Remix, under "Low level interactions",
 *      put any data such as 0x12345678 in CALLDATA and click Transact.
 *
 * Observe for every transaction (Remix console or Etherscan):
 *   gas limit, gas used (transaction cost / execution cost),
 *   gas price and transaction fee = gas used x gas price.
 * Reading functions marked `view` cost no gas when called from outside.
 */
contract StudentData {
    // ---------------------------------------------------------------- Structure
    struct Student {
        uint256 rollNo;
        string name;
        string department;
        uint8 marks;
    }

    // ---------------------------------------------------------------- Array
    Student[] private students;

    address public owner;

    event StudentAdded(uint256 rollNo, string name);
    event FallbackCalled(address sender, bytes data);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can do this");
        _;
    }

    // Add a new student record to the array.
    function addStudent(
        uint256 rollNo,
        string calldata name,
        string calldata department,
        uint8 marks
    ) external onlyOwner {
        require(marks <= 100, "Marks must be between 0 and 100");
        for (uint256 i = 0; i < students.length; i++) {
            require(students[i].rollNo != rollNo, "Roll number already exists");
        }
        students.push(Student(rollNo, name, department, marks));
        emit StudentAdded(rollNo, name);
    }

    // Number of students stored.
    function getStudentCount() external view returns (uint256) {
        return students.length;
    }

    // Student at a given position in the array.
    function getStudentByIndex(uint256 index) external view returns (Student memory) {
        require(index < students.length, "Index out of range");
        return students[index];
    }

    // Search the array for a roll number.
    function getStudentByRollNo(uint256 rollNo) external view returns (Student memory) {
        for (uint256 i = 0; i < students.length; i++) {
            if (students[i].rollNo == rollNo) {
                return students[i];
            }
        }
        revert("Student not found");
    }

    // All students.
    function getAllStudents() external view returns (Student[] memory) {
        return students;
    }

    // ---------------------------------------------------------------- Fallback
    // Runs when the contract is called with a function that does not exist.
    // It is not payable, so any Ether sent to the contract is rejected
    // and returned to the sender (nothing can get stuck here).
    fallback() external {
        emit FallbackCalled(msg.sender, msg.data);
    }
}
