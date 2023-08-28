class Endpoint:
    status = None

    def status_code_is_200(self):
        return self.status == 200
