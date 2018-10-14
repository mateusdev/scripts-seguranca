#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <errno.h>
#include <unistd.h>

#define LEN 4096

/*
	netecate allows you to connect to a service, only needing an IP and a port
*/

int main(int argc, char *argv[]){
	if(argc < 3){
		printf("USAGE: %s <ip> <port>\n", argv[0]);
		exit(1);
	}
	
	int sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if(sockfd == -1){
		perror("Socket creation error");
		exit(1);
	}

	char buffer[LEN];
	memset(buffer, 0x0, LEN);
	scanf("%4096s", buffer);
	buffer[LEN - 3] = '\r';
	buffer[LEN - 2] = '\n';
	buffer[LEN - 1] = '\0';

	struct sockaddr_in server;
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = inet_addr(argv[1]);
	server.sin_port = htons(atoi(argv[2]));

	if(connect(sockfd, (struct sockaddr *) &server, sizeof(server)) == -1){
		perror("Connection error");
		exit(1);
	}
	
	if(send(sockfd, buffer, sizeof(buffer), 0) < 0){
		perror("Send error");
		exit(1);
	}

	memset(buffer, 0x0, LEN);
	int valor = recv(sockfd, buffer, LEN, 0);
	buffer[valor - 1] = '\0';
	printf("%s", buffer);

	close(sockfd);

	return 0;
}
