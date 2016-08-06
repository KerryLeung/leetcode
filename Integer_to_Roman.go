func intToRoman(num int) string {
    RomanDict := [4][10]string{ { "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}, { "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"}, {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}, {"", "M", "MM", "MMM", "", "", "", "", "", ""} }
    
    return RomanDict[3][num / 1000] + 
            RomanDict[2][num % 1000 / 100] +
            RomanDict[1][num % 100 / 10] +
            RomanDict[0][num % 10]
}
