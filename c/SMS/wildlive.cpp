/**
	*  @filename   :   SMS.cpp
	*  @brief      :   Implements for sim7600c 4g hat raspberry pi demo
	*  @author     :   Kaloha from Waveshare
	*
	*  Copyright (C) Waveshare     April 27 2018
	*  http://www.waveshare.com / http://www.waveshare.net
	*
	* Permission is hereby granted, free of charge, to any person obtaining a copy
	* of this software and associated documnetation files (the "Software"), to deal
	* in the Software without restriction, including without limitation the rights
	* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	* copies of the Software, and to permit persons to  whom the Software is
	* furished to do so, subject to the following conditions:
	*
	* The above copyright notice and this permission notice shall be included in
	* all copies or substantial portions of the Software.
	*
	* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	* FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	* LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
	* THE SOFTWARE.
*/

#include "../arduPi.h"
#include "../sim7x00.h"
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <unistd.h>
#include <regex>
using namespace std;

// Pin definition
int POWERKEY = 6;

// TODO: add more standard message options

char phone_number[] = "15031234567"; // this is for use with other functions	
char welcome[] = "Welcome to Wildlive Remote, where you can receive live photo or video with a single text. Your number is new, please text a valid email address receive media";
char generic[] = "text 'photo' to receive a photo or 'vid' to receive a video";
char registered[] = "your phone number and email are saved, now text 'photo' or 'vid' to get your live media";
char conf[] = "request received, processing request";
string admin = "18027346892";
string off = "off";

void setup() {
	sim7600.PowerOn(POWERKEY);
}

bool valid_email(const string& email)
{
	//regex
   const regex pattern("(\\w+)(\\.|_)?(\\w*)@(\\w+)(\\.(\\w+))+");

   // compare regex to email
   return regex_match(email, pattern);
}

void listen() {
	
	// slow things down 5 second delay is fine, maybe more pending battery usage
	unistd::sleep(5);

	// vars
	char message[200];
	bool rec_msg = false;

	// check for message
	rec_msg = sim7600.ReceivingShortMessage(message);

	// if there's a message
	if (rec_msg == true)
	{
		string msg(message);
		string ph_num;
		string text;

		// read over message
		for (int i = 0; i < msg.length(); i++)
		{
			// find the start of the phone number and store it
			if (msg[i] == '+')
			{
				ph_num = msg.substr(i+1, 11);
				cout << ph_num << endl;
			}

			// the text of the message begins on the 2nd line of message
			else if (i > 56 && msg[i] == '\n')
			{
				text = msg.substr(56, i-57);
				cout << "full message: " << msg << endl;
				break;
			}
		}

		// set the string to lower case
		transform(text.begin(), text.end(), text.begin(), ::tolower);

		// If Admin sent the command off, remote shutdown
		if (text.compare(off) == 0 && ph_num.compare(admin) == 0)
		{
			cout << "Remote Off..." << endl;
			exit(0);
		}
	
		// check if its a known phone number if not send welcome message
		ifstream fi;
		string line;
		bool known = false;
		fi.open("/home/pi/WildLive/logs/stored_numbers.txt");
		while (getline(fi,line))
		{
			string stored_num = line.substr(0, line.find(','));
			if (stored_num.compare(ph_num) == 0)
			{
				known = true;
				break;
			}
		}
		fi.close();
		
		//check if they sent an email
		bool is_email = valid_email(text);

		// if its just a new number, send the welcome message
		if (known == false && is_email == false)
		{
			// convert the phone number
			char ph_num_char[ph_num.size() + 1];
			strcpy(ph_num_char, ph_num.c_str());

			// send the basic return message back to the sender
			sim7600.SendingShortMessage(ph_num_char, welcome);
			strcpy(ph_num_char, "0000000000");
		}

		// if its a new number and email store them and send registered message
		if (known == false && is_email == true)
		{
			// save phone number and email
			ofstream f;
			f.open("/home/pi/WildLive/logs/stored_numbers.txt", fstream::app);
			f << ph_num << ',' << text << endl;
			f.close();

			// convert the phone number
			char ph_num_char[ph_num.size() + 1];
			strcpy(ph_num_char, ph_num.c_str());

			// send the basic return message back to the sender
			sim7600.SendingShortMessage(ph_num_char, registered);
			strcpy(ph_num_char, "0000000000");
		}

		// otherwise send the message off for processing and send a confirmation text
		else 
		{
			// convert the phone number
			char ph_num_char[ph_num.size() + 1];
			strcpy(ph_num_char, ph_num.c_str());

			// send the basic return message back to the sender
			sim7600.SendingShortMessage(ph_num_char, conf);
			strcpy(ph_num_char, "0000000000");

			// find their email
			string email;
			fi.open("/home/pi/WildLive/logs/stored_numbers.txt");
			while (getline(fi,line))
			{
				string stored_num = line.substr(0, line.find(','));
				if (stored_num.compare(ph_num) == 0)
				{
					email = line.substr(line.find(','), line.length());
				}
			}
			fi.close();

			// Write phone number and message out to a file for processing and execution
			ofstream f;
			f.open("/home/pi/WildLive/logs/sms_input.txt");
			f << ph_num << ',' << email << ',' << text << endl;
			f.close();
		}	
	}
}

int main() {
	setup();
	while(true)
	{
		listen();
	}

	printf("program finished successfully\n");
	return (0);
}
