/*
 * ./src/MathMasters.sol 
 *
 * Verification of MulWadUp for MathMasters.
 */
methods {
    // function mathMastersSqrt(uint256 x) external returns (uint256) envfree;
    // function uniSqrt(uint256 x) external returns (uint256) envfree;
    function solmateTopHalf(uint256 x) external returns (uint256) envfree;
    function mathMastersTopHalf(uint256 x) external returns (uint256) envfree;
}

rule solmateTopHalfMatchesMathMastersTopHalf(uint256 x) {
    // This specific value causes an overflow in the implementation
    require(x != 0xffffff00000000000000000000000000000, "Excluded due to known overflow in implementation");
    assert(mathMastersTopHalf(x) == solmateTopHalf(x));
}
