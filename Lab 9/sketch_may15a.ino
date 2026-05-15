int LED1pin = 43;
int LED2pin = 44;
int LED3pin = 45;
int LED4pin = 46;
int button1pin = 38;
int button2pin = 39;

int systemState = LOW;      
int lastBut1State = LOW;    

int currentMode = 1;        
int lastBut2State = LOW;    

unsigned long previousMillis = 0;
const long interval = 1000; 

int blinkState = LOW;       
int sequenceStep = -1;      

void setup() {
  pinMode(LED1pin, OUTPUT);
  pinMode(LED2pin, OUTPUT);
  pinMode(LED3pin, OUTPUT);
  pinMode(LED4pin, OUTPUT);
  pinMode(button1pin, INPUT);
  pinMode(button2pin, INPUT);
}

void loop() {
  int but1State = digitalRead(button1pin);
  
  if (but1State != lastBut1State) {
    if (but1State == HIGH) { 
      if (systemState == LOW) {
        systemState = HIGH;
        previousMillis = millis() - interval; 
      } else {
        systemState = LOW;
        digitalWrite(LED1pin, LOW);
        digitalWrite(LED2pin, LOW);
        digitalWrite(LED3pin, LOW);
        digitalWrite(LED4pin, LOW);
      }
    }
    delay(50); 
  }
  lastBut1State = but1State;

  int but2State = digitalRead(button2pin);
  
  if (but2State != lastBut2State) {
    if (but2State == HIGH) {
      currentMode++;
      if (currentMode > 3) {
        currentMode = 1; 
      }
      
      digitalWrite(LED1pin, LOW);
      digitalWrite(LED2pin, LOW);
      digitalWrite(LED3pin, LOW);
      digitalWrite(LED4pin, LOW);
      sequenceStep = -1;
      previousMillis = millis() - interval; 
    }
    delay(50); 
  }
  lastBut2State = but2State;

  if (systemState == HIGH) {
    
    unsigned long currentMillis = millis(); 

    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis; 
      
      if (currentMode == 1) {
        if (blinkState == LOW) {
          blinkState = HIGH;
        } else {
          blinkState = LOW;
        }
        digitalWrite(LED1pin, blinkState);
        digitalWrite(LED2pin, blinkState);
        digitalWrite(LED3pin, blinkState);
        digitalWrite(LED4pin, blinkState);
      } 
      
      else if (currentMode == 2) {
        sequenceStep++; 
        if (sequenceStep > 3) sequenceStep = 0; 

        if (sequenceStep == 0) {
          digitalWrite(LED1pin, HIGH); digitalWrite(LED2pin, LOW); digitalWrite(LED3pin, LOW); digitalWrite(LED4pin, LOW);
        } else if (sequenceStep == 1) {
          digitalWrite(LED1pin, LOW); digitalWrite(LED2pin, HIGH); digitalWrite(LED3pin, LOW); digitalWrite(LED4pin, LOW);
        } else if (sequenceStep == 2) {
          digitalWrite(LED1pin, LOW); digitalWrite(LED2pin, LOW); digitalWrite(LED3pin, HIGH); digitalWrite(LED4pin, LOW);
        } else if (sequenceStep == 3) {
          digitalWrite(LED1pin, LOW); digitalWrite(LED2pin, LOW); digitalWrite(LED3pin, LOW); digitalWrite(LED4pin, HIGH);
        }
      } 
      
      else if (currentMode == 3) {
        sequenceStep++;
        if (sequenceStep > 3) sequenceStep = 0;

        if (sequenceStep == 0) {
          digitalWrite(LED1pin, LOW); digitalWrite(LED2pin, LOW); digitalWrite(LED3pin, LOW); digitalWrite(LED4pin, HIGH);
        } else if (sequenceStep == 1) {
          digitalWrite(LED1pin, LOW); digitalWrite(LED2pin, LOW); digitalWrite(LED3pin, HIGH); digitalWrite(LED4pin, LOW);
        } else if (sequenceStep == 2) {
          digitalWrite(LED1pin, LOW); digitalWrite(LED2pin, HIGH); digitalWrite(LED3pin, LOW); digitalWrite(LED4pin, LOW);
        } else if (sequenceStep == 3) {
          digitalWrite(LED1pin, HIGH); digitalWrite(LED2pin, LOW); digitalWrite(LED3pin, LOW); digitalWrite(LED4pin, LOW);
        }
      }
    }
  }
}