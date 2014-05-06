import zerorpc

c = zerorpc.Client()
c.connect("tcp://10.1.34.235:4242")
print c.hello("Test RPC")
