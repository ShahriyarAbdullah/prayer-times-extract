class Month:
    def __init__(self, month):
        self.month = month
    
    def daycalc(self):
        if self.month in ["Apr", "Sep", "Oct", "Nov"]:
            return 30
        elif self.month in ["Jan", "Mar", "May", "Jun", "Jul", "Aug", "Dec"]:
            return 31
        elif self.month == "Feb":
            return 28
        elif self.month == "Fel":
            return 29
        else:
            return "Invalid month"
