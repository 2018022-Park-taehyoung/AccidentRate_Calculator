class 재해율:
    def __init__(self, AW, DS, HD, DW, YW, DR_list):
        self.AW = int(AW)       # 평균근로자수
        self.DS = int(DS)       # 재해건수
        self.HD = int(HD)       # 휴업일수
        self.DW = int(DW)       # 일 근무시간
        self.YW = int(YW)       # 연간 근무일수
        self.DR_list = DR_list  # 장애등급 리스트
        self.DD = 0             # 장애등급별 손실일수를 모두 더한 값
        self.frequency = 0      # 도수율
        self.severity = 0       # 강도율
        self.Indicator = 0      # 종합재해지수

        for DR in DR_list:
            if DR == 1 or DR == 2 or DR == 3 or DR == '사망':
                self.DD += 7500
            elif DR == 4:
                self.DD += 5500
            elif DR == 5:
                self.DD += 4000
            elif DR == 6:
                self.DD += 3000
            elif DR == 7:
                self.DD += 2000
            elif DR == 8:
                self.DD += 1500
            elif DR == 9:
                self.DD += 1000
            elif DR == 10:
                self.DD += 600
            elif DR == 11:
                self.DD += 400
            elif DR == 12:
                self.DD += 200
            elif DR == 13:
                self.DD += 100
            elif DR == 14:
                self.DD += 50
            else:
                self.DD += 0

    def Fre(self):
        self.frequency = (self.DS / (self.AW * self.DW * self.YW)) * 10 ** 6
        print("도수율은 " + str(self.frequency) + "입니다.")

    def Sev(self):
        self.severity = ((self.HD * (self.YW / 365) + self.DD) / (self.AW * self.DW * self.YW)) * 1000
        print("강도율은 " + str(self.severity) + "입니다.")

    def FSI(self):
        self.Indicator = (self.frequency * self.severity) ** (1/2)
        print("종합재해지수는 " + str(self.Indicator) + "입니다.")
