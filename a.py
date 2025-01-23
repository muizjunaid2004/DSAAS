def hasDuplicate(nums):
        
        setCheck = set()

        for num in nums:
            if num in setCheck:
                return True
            setCheck.add(num)
            
        print(setCheck)

        return False
    
print(hasDuplicate([1,11,2]))