// SPDX-License-Identifier: MIT

pragma solidity ^0.8.28;

import "./Eldorion.sol";

contract EldorionSlayer {
    Eldorion target;

    constructor(address _target) {
        target = Eldorion(_target);
    }

    function slay() external {
        target.attack(100);
        target.attack(100);
        target.attack(100);
    }
}