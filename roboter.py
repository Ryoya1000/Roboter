class Roboter(object):

    def ask_question(self):
        self.name = input('こんにちは！私Robokoです。あなたの名前はなんですか？:')
        # self.csv_data = self.read_csv()
        # print(self.csv_data)
        self.restaurant = input("%sさん。どこのレストランが好きですか？" % (self.name))
        if self.restaurant is not '':
            self.export_csv(self.restaurant)
            print('%sさん。ありがとうございました。\n良い一日を！さよなら。' % (self.name))
        else:
            print('未回答です。')

    def export_csv(self, restaurant):
        with open('restaurant.csv', 'w') as f:
            f.write("%s,1" % (self.restaurant))

    def read_csv(self):
        with open('restaurant.csv', 'r') as f:
            line = f.readline()
            return line

roboter = Roboter()
roboter.ask_question()
