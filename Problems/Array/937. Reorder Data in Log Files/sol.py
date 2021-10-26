class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_logs = []
        let_logs_sor = []
        dig_logs = []

        for log in logs:
            if log.split(' ')[1].isdigit():
                dig_logs.append(log)
            else:
                let_logs.append(log)
                t = log.split()[1:]
                t = ' '.join(t)
                let_logs_sor.append(t)

        let_logs_sor, let_logs = zip(*sorted(zip(let_logs_sor, let_logs)))

        return list(let_logs) + dig_logs
