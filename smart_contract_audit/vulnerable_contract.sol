pragma solidity ^0.8.0;

        contract Test {
            address public owner;

            constructor() {
                owner = msg.sender;
            }

            function withdraw() public {
                require(tx.origin == owner);
                payable(msg.sender).transfer(address(this).balance);
            }
        }
