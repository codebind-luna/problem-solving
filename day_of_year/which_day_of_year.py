class Solution:
    def dayOfYear(self, date: str) -> int:
        months_dic = {
			0: 0,
			1: 31,
			2: 59,
			3: 90,
			4: 120,
			5: 151,
			6: 181,
			7: 212,
			8: 243,
			9: 273,
			10: 304,
			11: 334,
			12: 365,
		}
        year, month, day = list(map(int, date.split("-")))
        
        def is_leap_year(year):
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return True
            else:
                return False
            
        if is_leap_year(year) and  month > 2:
            return months_dic[month - 1] + day + 1
        else:
            return months_dic[month - 1] + day
            
        
        