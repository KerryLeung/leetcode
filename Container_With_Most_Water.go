func maxArea(height []int) int {
    if len(height) < 2{
        return 0
    }
    
    res := 0
    local_res := 0
    for i := 0; i < len(height); i++{
        if i == len(height) - 1{
            break
        }else{
            for j := i+1; j < len(height); j++{
                if height[i] > height[j]{
                    local_res = height[j] * (j - i) 
                }else{
                    local_res = height[i] * (j - i) 
                }
                
                if local_res > res{
                    res = local_res
                }
            }
        }
    }
    return res
}
