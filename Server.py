import sys, socket

from ServerWorker import ServerWorker
import signal
def signal_handler(code, frame):
	print("Server shut down")
	sys.exit()

class Server:	
	
	def main(self):
		try:
			SERVER_PORT = int(sys.argv[1])
		except:
			print "[Usage: Server.py Server_port]\n"
		rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		rtspSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		rtspSocket.bind(('', SERVER_PORT))
		rtspSocket.listen(5)        
		signal.signal(signal.SIGINT, signal_handler)
		# Receive client info (address,port) through RTSP/TCP session
		while True:
			clientInfo = {}
			
			clientInfo['rtspSocket'] = rtspSocket.accept()
			
			ServerWorker(clientInfo).run()		

if __name__ == "__main__":
	(Server()).main()
	


