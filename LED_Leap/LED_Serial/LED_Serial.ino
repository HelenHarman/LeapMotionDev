/**
 @Description : 
 
 @Created : September 2014 By Helen Harman  
 
 @Modified: 20th September 2014


*/
void setup()
{
  Serial.begin(9600);
  // sets the pins with the LEDs attached
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(2, OUTPUT);  
}


/**
  Gets called whenever something gets written to Serial.

*/
void serialEvent()
{
  Serial.println("serialEvent");
  const int NOTES[] = {262, 294, 330, 349};
  int incomingByte = 0; 
  int pinNum = 2;

  // 6pins being used. So must loop 12times due to -1 being picked up from 
  // serial.read() some of the time.
  for (int i = 0; i < 12; i++)
  {
    // read the incoming byte:
    incomingByte = Serial.read();

    // say what you got:
    Serial.print("I received: ");
    Serial.print(incomingByte, DEC);
    //Serial.print(" From : ");
    //Serial.println(i);    
    Serial.print(" PIN = ");
    Serial.println(pinNum);
    
    if (pinNum == 7) // Pin with piezo attached
    {      
      if (incomingByte == 0) // no tone with thumb. And when all fingers above 100.
      {
        noTone(pinNum);
      }
      else if ((incomingByte > 0) && (incomingByte <= sizeof(NOTES)))
      {
        tone(pinNum, NOTES[incomingByte-1]);
      }            
    }
    else // Pin with LED attached 
    {
      if (incomingByte == 1) // turn LED on
      {
        digitalWrite(pinNum, HIGH);
        pinNum++;
      }
      else if (incomingByte == 0) // turn LED off
      {
        digitalWrite(pinNum, LOW);
        pinNum++;
      }   
    } 
  } 
}



/**
Arduino must have loop() function. 
*/
void loop()
{
  
//empty function

}
