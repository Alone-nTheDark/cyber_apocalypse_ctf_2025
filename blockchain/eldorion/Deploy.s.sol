// SPDX-License-Identifier: MIT

pragma solidity ^0.8.28;

import "forge-std/Script.sol";
import "../src/Eldorion.sol";
import "../src/EldorionSlayer.sol";
import "../src/Setup.sol";

contract Deploy is Script {
    function run() external {
        vm.startBroadcast();

        address targetAddress = 0x9243620c28B1e5A0cbBC6D9461fB07e8f540bED8;

        EldorionSlayer slayer = new EldorionSlayer(targetAddress);

        vm.stopBroadcast();
    }
}
