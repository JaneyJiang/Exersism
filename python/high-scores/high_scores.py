class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        self.scores_sort = sorted(scores,reverse=True)

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return self.scores_sort[0]

    def personal_top(self):
        return self.scores_sort[:3]
        
    def report(self):
        latest_report = "Your latest score was {}. ".format(self.latest())
        diff = self.personal_best()-self.latest()
        personal_report = "That's {} short of your personal best!".format(diff) if diff else "That's your personal best!"
        return latest_report+personal_report


