# Findings

## High
### [H-1] `MathMasters::sqrt` incorrectly checks the `lt` of a right shift

```javascript
            // 87112285931760246646623899502532662132735 == 0xffffffffffffffffffffffffffffffffff 
            let r := shl(7, lt(87112285931760246646623899502532662132735, x))
            // 4722366482869645213695 == 0xffffffffffffffffff
            r := or(r, shl(6, lt(4722366482869645213695, shr(r, x))))
            // 1099511627775 == 0xffffffffff
            r := or(r, shl(5, lt(1099511627775, shr(r, x))))
            // @audit this should be 16777215 / 0xffffff
            // Right now, it's 0xffff2a!
@>          r := or(r, shl(4, lt(16777002, shr(r, x))))
```

### [H-2] `MathMasters::mulWadUp` function does not revert as expected

Corrected Function:
```diff
    function mulWadUp(uint256 x, uint256 y) internal pure returns (uint256 z) {
        /// @solidity memory-safe-assembly
        assembly {
            // Equivalent to `require(y == 0 || x <= type(uint256).max / y)`.
+           if mul(y, gt(x, div(not(0), y))) {
-           if mul(y, gt(x, or(div(not(0), y), x))) {
                mstore(0x00, 0xbac65e5b) // `MulWadFailed()`.
                revert(0x1c, 0x04)
            }
            z := add(iszero(iszero(mod(mul(x, y), WAD))), div(mul(x, y), WAD))
        }
    }
```

## Medium

## Low 
### [L-1] Solidity version `0.8.3` does not allow custom errors, breaking compliation. 

### [L-2] Wrong function selector for `MathMasters::MathMasters__FullMulDivFailed()` custom error
- The function selector of`MathMasters__FullMulDivFailed()` is `0x41672c55`, yet `0xae47f702` is being used. 

## Info

### [I-1] Custom error codes are written to the solidity free memory pointer's position 

It doesn't *do* anything... but like why are you doing that you masochist. 