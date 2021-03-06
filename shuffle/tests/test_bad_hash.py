from test import TestProtocolCase, bad_client_wrong_broadcast
import random

class TestProtocol(TestProtocolCase):

    def test_001_cheat_in_sending_different_keys(self):
        protocolThreads = self.make_clients_threads(with_print = True, number_of_clients = self.number_of_players - 1)
        bad_thread = self.make_bad_client(bad_client_wrong_broadcast, with_print = True)
        protocolThreads.append(bad_thread)
        random.shuffle(protocolThreads)
        self.start_protocols(protocolThreads)
        done = False
        while not done:
            completes = [self.is_protocol_complete(p) for p in protocolThreads[1:]]
            done = all(completes)
        self.stop_protocols(protocolThreads)
        tx = protocolThreads[1].protocol.tx.raw
        for pThread in protocolThreads[2:]:
            self.assertEqual(tx, pThread.protocol.tx.raw)

    def test_002_cheat_in_sending_different_outputs(self):
        protocolThreads = self.make_clients_threads(with_print = True, number_of_clients = self.number_of_players - 1)
        bad_thread = self.make_bad_client(bad_client_output_vector, with_print = True)
        self.start_protocols(protocolThreads)
        protocolThreads.append(bad_thread)
        time.sleep(1)
        bad_thread.start()
        done = False
        while not done:
            completes = [self.is_protocol_complete(p) for p in protocolThreads[:-1]]
            done = all(completes)
        self.stop_protocols(protocolThreads)
        tx = protocolThreads[0].protocol.tx.raw
        for pThread in protocolThreads[:-1]:
            self.assertEqual(tx, pThread.protocol.tx.raw)
