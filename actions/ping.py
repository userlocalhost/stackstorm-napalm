from lib.action import NapalmBaseAction


class NapalmPing(NapalmBaseAction):
    """Run a ping from a network device via NAPALM
    """

    def run(self, destination, source, ttl=255, pingtout=2, size=100, count=5, htmlout=False,
            **std_kwargs):

        try:

            with self.get_driver(**std_kwargs) as device:

                result = {'raw': device.ping(destination, source, ttl, pingtout, size, count)}

                if htmlout:
                    result['html'] = self.html_out(result['raw'])

        except Exception, e:
            self.logger.error(str(e))
            return (False, str(e))

        return (True, result)
