1. 서보모터 구동 실습코드
#include <Servo.h>
Servo myservo;
void setup() {
  myservo.attach(2);
}
void loop() {
  myservo.write(0);
  delay(3000);
  myservo.write(90);
  delay(3000);
  myservo.write(180);
  delay(3000);
} 

1. 서보모터 구동 실습코드(2)
#include <Servo.h> 
Servo servo;
void setup() {
  servo.attach(2);  
  Serial.begin(9600);  
  servo.write(90); 
  delay(1000);
}
void loop() {
}

2. 초음파 센서 실습코드
inttrigPin = 13;
intechoPin = 12;
void setup() {
  Serial.begin(9600);      // 시리얼 속도 설정
  pinMode(echoPin, INPUT);  // echoPin 입력
  pinMode(trigPin, OUTPUT); // trigPin 출력
}
void loop() {
  longduration, distance;
  digitalWrite(trigPin, HIGH);                       // trigPin에서 초음파 발생(echoPin도 HIGH)
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);                 // echoPin 이 HIGH를 유지한 시간을 저장 한다.
  distance = ((float)(340* duration)/ 10000)/ 2; 
  Serial.print("distance:");                         // 물체와 초음파 센서간 거리를 표시
  Serial.print(distance);
  Serial.println(" cm");
  delay(500);
}



3. 라인트레이서 구동 실습코드
void setup() {
  Serial.begin(9600);
}
void loop() {
  intval_1 = analogRead(A3);
  intval_2 = analogRead(A4);
  intval_3 = analogRead(A5);
  
  Serial.print("1:");
  Serial.print(val_1);
  Serial.print(" 2:");
  Serial.print(val_2);
  Serial.print(" 3:");
  Serial.println(val_3);
}



4. DC모터 드라이버 구동 실습코드
intRightMotor_E_pin = 5;     // 오른쪽 모터의 Enable & PWM
intRightMotor_1_pin = 8;     // 오른쪽 모터 제어선 IN1
intRightMotor_2_pin = 9;    // 오른쪽 모터 제어선 IN2
intLeftMotor_3_pin = 10;     // 왼쪽 모터 제어선 IN3
intLeftMotor_4_pin = 11;     // 왼쪽 모터 제어선 IN4
intLeftMotor_E_pin = 6;     // 왼쪽 모터의 Enable & PWM
void SmartCar_Go();
void SmartCar_Back();
//좌우 모터 속도 조절, 설정 가능 최대 속도 : 255
intL_MotorSpeed = 153;// 왼쪽 모터 속도
intR_MotorSpeed = 153;// 오른쪽 모터 속도
void setup() {
  pinMode(RightMotor_E_pin, OUTPUT);       // 출력모드로 설정
  pinMode(RightMotor_1_pin, OUTPUT);
  pinMode(RightMotor_2_pin, OUTPUT);
  pinMode(LeftMotor_3_pin, OUTPUT);
  pinMode(LeftMotor_4_pin, OUTPUT);
  pinMode(LeftMotor_E_pin, OUTPUT);
}
void loop() {
  SmartCar_Go();
  delay(3000);
  SmartCar_Back();
  delay(3000);
}

void SmartCar_Go() {      // 전진
  Serial.println("Forward");
  digitalWrite(RightMotor_1_pin, HIGH);
  digitalWrite(RightMotor_2_pin, LOW);
  digitalWrite(LeftMotor_3_pin, HIGH);
  digitalWrite(LeftMotor_4_pin, LOW);
  analogWrite(RightMotor_E_pin, L_MotorSpeed);
  analogWrite(LeftMotor_E_pin, R_MotorSpeed);
}

void SmartCar_Back() {      // 후진
  Serial.println("Backward");
  digitalWrite(RightMotor_1_pin, LOW);
  digitalWrite(RightMotor_2_pin, HIGH);
  digitalWrite(LeftMotor_3_pin, LOW);
  digitalWrite(LeftMotor_4_pin, HIGH);
  analogWrite(RightMotor_E_pin, L_MotorSpeed);
  analogWrite(LeftMotor_E_pin, R_MotorSpeed);
}

5. 시리얼 통신 제어 (직진, 후진)
int RightMotor_E_pin = 5 ;    // 오른쪽 모터의 Enable &PWM
int LeftMotor_E_pin = 6 ;    // 왼쪽 모터의 Enable &PWM
int RightMotor_1_pin = 8 ;    // 오른쪽 모터 제어선 IN1
int RightMotor_2_pin = 9 ;    // 오른쪽 모터 제어선 IN2
int LeftMotor_3_pin = 10 ;    // 왼쪽 모터 제어선 IN3
int LeftMotor_4_pin = 11 ;    // 왼쪽 모터 제어선 IN4
//좌우 모터 속도 조절, 설정 가능 최대 속도 : 255
int L_MotorSpeed = 153 ; // 왼쪽 모터 속도
int R_MotorSpeed = 153 ; // 오른쪽 모터 속도
void setup (){
  pinMode (RightMotor_E_pin, OUTPUT );    // 출력모드로 설정
  pinMode (RightMotor_1_pin, OUTPUT );
  pinMode (RightMotor_2_pin, OUTPUT );
  pinMode (LeftMotor_3_pin, OUTPUT );
  pinMode (LeftMotor_4_pin, OUTPUT );
  pinMode (LeftMotor_E_pin, OUTPUT );
  Serial .begin (9600 );            
  Serial .println ("Welcome");
}
void loop (){
  if (Serial .available ()){          
   char command = Serial .read ();      
   Serial .print ("Recived command : ");
   if (command == 'g'){           
    motor_role (HIGH, HIGH );
    Serial .println ("직진"); 
   }
   else if (command == 'b'){        
    motor_role (LOW, LOW ); 
    Serial .println진 ("후진"); 
   }
   else {
    Serial .println ("Wrong command");    
   }
  }
}
void motor_role (int R_motor , int L_motor){
   digitalWrite (RightMotor_1_pin, R_motor );
   digitalWrite (RightMotor_2_pin, !R_motor );
   digitalWrite (LeftMotor_3_pin, L_motor );
   digitalWrite (LeftMotor_4_pin, !L_motor );
   analogWrite (RightMotor_E_pin, R_MotorSpeed );  
   analogWrite (LeftMotor_E_pin, L_MotorSpeed );
}


6. 초음파센서를 활용한 장애물 회피 자율주행 테스트
#include <Servo.h>
Servo Servo;
//출력핀(trig)과 입력핀(echo) 설정
inttrigPin = 13;                 // 디지털 13번 핀에 연결
intechoPin = 12;                 // 디지털 12번 핀에 연결
intUltra_d = 0;
intval = 0;                   // 좌우 경로 설정 변수
   
intRightMotor_E_pin = 5;      // 오른쪽 모터의 Enable & PWM
intLeftMotor_E_pin = 6;       // 왼쪽 모터의 Enable & PWM
intRightMotor_1_pin = 11;      // 오른쪽 모터 제어선 IN1
intRightMotor_2_pin = 10;      // 오른쪽 모터 제어선 IN2
intLeftMotor_3_pin = 9;      // 왼쪽 모터 제어선 IN3
intLeftMotor_4_pin = 8;      // 왼쪽 모터 제어선 IN4
//좌우 모터 속도 조절, 설정 가능 최대 속도 : 255
intL_MotorSpeed = 153;// 왼쪽 모터 속도
intR_MotorSpeed = 153;// 오른쪽 모터 속도
void setup() { 
  Servo.attach(2);                      // 서보모터 PWM 디지털입출력 2번핀 연결
  
  pinMode(echoPin, INPUT);                 // echoPin 입력
  pinMode(trigPin, OUTPUT);                // trigPin 출력
  
  pinMode(RightMotor_E_pin, OUTPUT);       // 출력모드로 설정
  pinMode(RightMotor_1_pin, OUTPUT);
  pinMode(RightMotor_2_pin, OUTPUT);
  pinMode(LeftMotor_3_pin, OUTPUT);
  pinMode(LeftMotor_4_pin, OUTPUT);
  pinMode(LeftMotor_E_pin, OUTPUT);
  Serial.begin(9600);                      // PC와의 시리얼 통신 9600bps로 설정
  Serial.println("Welcome!");
}
void loop() { 
  Ultra_d = Ultrasonic();
  Serial.println(Ultra_d);
  motor_role(HIGH, HIGH); // 직진
  if(Ultra_d < 250) {
    if (Ultra_d < 150) {
      Serial.println("150 이하.");
      motor_role(LOW, LOW);// 후진
      delay(1000);
      analogWrite(RightMotor_E_pin, 0);  
      analogWrite(LeftMotor_E_pin, 0);
      delay(200);
    }
    else {
      analogWrite(RightMotor_E_pin, 0);  
      analogWrite(LeftMotor_E_pin, 0);
      delay(200);
      Serial.println("150 이상.");
      val =  Servo_con();
      if (val == 0) {
        Serial.println("우회전.");
        analogWrite(RightMotor_E_pin, 0);  
        analogWrite(LeftMotor_E_pin, 0);
        delay(500);
        motor_role(LOW, LOW); // 후진
        delay(500);
        motor_role(LOW, HIGH); // 우회전
        delay(800);
      }
      else if (val == 1) {
        Serial.println("좌회전.");
        analogWrite(RightMotor_E_pin, 0);  
        analogWrite(LeftMotor_E_pin, 0);
        delay(500);
        motor_role(LOW, LOW); // 후진
        delay(500);
        motor_role(HIGH, LOW); // 좌회전
        delay(800);
      }
    }
  }
}
void motor_role(int R_motor, int L_motor){
   digitalWrite(RightMotor_1_pin, R_motor);
   digitalWrite(RightMotor_2_pin, !R_motor);
   digitalWrite(LeftMotor_3_pin, L_motor);
   digitalWrite(LeftMotor_4_pin, !L_motor);
   
   analogWrite(RightMotor_E_pin, R_MotorSpeed); // 우측 모터 속도값
   analogWrite(LeftMotor_E_pin, L_MotorSpeed);  // 좌측 모터 속도값  
}
int Ultrasonic(){
  longduration, distance;
  digitalWrite(trigPin, HIGH);     // trigPin에서 초음파 발생(echoPin도 HIGH)        
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);  // echoPin 이 HIGH를 유지한 시간을 저장 한다.
  distance = ((float)(340* duration)/ 1000)/ 2; 
  //Serial.print("DIstance:");        // 물체와 초음파 센서간 거리를 표시.        
  //Serial.println(distance);
  returndistance;
}
int Servo_con(){
  Servo.write(30);
  delay(300);
  intUlt_30 = Ultrasonic();
  delay(700);
  Servo.write(150);
  delay(300);
  intUlt_150 = Ultrasonic();
  delay(700);
  if(Ult_30 > Ult_150){
     val = 1;
  }
  else{
     val = 0;
  }
  Servo.write(90);
  
  returnval;
}

7. led센서를 활용하여 제작한 신호등 작동 테스트
#define LED_R 3      // R의 핀 번호 3
#define LED_Y 4      // Y의 핀 번호 4
#define LED_G 5      // G의 핀 번호 5
 
void setup() {
  // put your setup code here, to run once:
  pinMode(LED_R, OUTPUT);
  pinMode(LED_Y, OUTPUT);
  pinMode(LED_G, OUTPUT);
}
 
void loop() {
  turnOffAll();                 // LED 다 끕니다.
  
  digitalWrite(LED_R, HIGH);    // 빨간 불 켜기
  delay(3000);                  // 3초간 유지
  turnOffAll();                 // 불 다 끄기
  
  digitalWrite(LED_G, HIGH);    // 초록 불 켜기
  delay(3000);                  // 3초간 유지
  turnOffAll();                 // 불 다 끄기
 
 digitalWrite(LED_Y, HIGH);     // 노란 불 켜기
  delay(2000);                  // 2초간 유지
  turnOffAll();                 // 불 다 끄기
 
}
 
void turnOffAll() {             // turnOffAll 함수 정의
  digitalWrite(LED_R, LOW);     // 빨간 불 끄기
  digitalWrite(LED_Y, LOW);     // 노란 불 끄기
  digitalWrite(LED_G, LOW);     // 초록 불 끄기
}

8. 파이썬-아두이노 제어를 통한 시리얼 통신테스트
[파이썬]
import serial
arduino = serial.Serial('COM4',9600)


while(1):
   c=input()
   if c =='q':
     break    
   else:
     c=c.encode('utf-8')
     arduino.write(c)


[아두이노]
#include <Servo.h>
Servo myservoH;  // create servo object to control a servo
Servo myservoV;
int posH = 90 ;
int posV = 90 ;
void setup (){
 myservoH .attach (2 );  // 서보모터를 쉴드의 2번에 연결한다.
 Serial .begin (9600 );
}
void loop (){
 while (Serial .available () >0 ){
   long value = Serial .parseInt ();
   int backUpH = posH;
   int backUpV = posV;
   switch (value ){
    case 1 :
     //posH = posH - 5; 같은 표현이다 posH -= 5;
     posH -= 30 ;
     break ;
    case 2 :
     posH += 30 ;
     break ;
    case 3 :
     posV -= 30 ;
     break ;
    case 4 :
     posV += 30 ;
     break ;
   }
   if (posH<0 || posH>180 ){
    posH=backUpH;
   }
   if (posV<0 || posV>180 ){
    posV=backUpV;
   }
   myservoH .write (posH );
   myservoV .write (posV );
 }
 
}



9. 라인트레이서, 초음파센서 코드 (if, else if문)
#include <Servo.h>               // 서보 라이브러리
Servo Servo;
//출력핀(trig)과 입력핀(echo)
inttrigPin = 13;                 // 디지털 13번 핀에 연결
intechoPin = 12;                 // 디지털 12번 핀에 연결
intUltra_d = 0;                  // 초음파 센서
intval = 0;                   // 좌우 경로 설정 변수
   
intRightMotor_E_pin = 5;      // 오른쪽 모터 전원부 5번 연결핀
intLeftMotor_E_pin = 6;       // 왼쪽 모터 전원부 6번 연결핀
intRightMotor_1_pin = 8;      // 오른쪽 모터  8번 IN1
intRightMotor_2_pin = 9;      // 오른쪽 모터  9번 IN2
intLeftMotor_3_pin = 10;      // 왼쪽 모터  10번 IN3
intLeftMotor_4_pin = 11;      // 왼쪽 모터  11번 IN4
//모터 속도 조절, 최대속도 : 255
intL_MotorSpeed = 153;// 왼쪽 모터 속도
intR_MotorSpeed = 153;// 오른쪽 모터 속도
intL_Line = A5;// 왼쪽 라인트레이서 센서 - 확장쉴드 A5
intC_Line = A4;// 가운데 라인트레이서 센서 - 확장쉴드 A4
intR_Line = A3;// 오른쪽 라인트레이서 센서 - 확장쉴드 A3
intSL = 1;
intSC = 1;
intSR = 1;
 // 부품 셋업
void setup() {
  Servo.attach(2);                      // 서보모터 PWM 디지털입출력 2번핀 연결
  pinMode(echoPin, INPUT);                 // echoPin 입력
  pinMode(trigPin, OUTPUT);                // trigPin 출력
  // 모터 핀 설치
  pinMode(RightMotor_E_pin, OUTPUT);// 오른쪽 모터 전원부 출력
  pinMode(LeftMotor_E_pin, OUTPUT);// 왼쪽 모터 전원부 출력
  pinMode(RightMotor_1_pin, OUTPUT);// 오른쪽 모터 앞바퀴 출력
  pinMode(RightMotor_2_pin, OUTPUT);// 오른쪽 모터 뒷바퀴 출력
  pinMode(LeftMotor_3_pin, OUTPUT);// 왼쪽 모터 앞바퀴 출력
  pinMode(LeftMotor_4_pin, OUTPUT);// 왼쪽 모터 뒷바퀴 출력
  Serial.begin(9600);   // PC와의 시리얼 통신 값 9600
  Serial.println("Activate!");// 통신에 성공했을 경우, 시리얼 모니터 창에 Activate! 출력
}
 // 라인트레이서 값 읽기
void loop() {
  intL = digitalRead(L_Line);
  intC = digitalRead(C_Line);
  intR = digitalRead(R_Line);

  Serial.print("digital : "); 
  Serial.print(L); 
  Serial.print(", "); 
  Serial.print(C); 
  Serial.print(", "); 
  Serial.print(R); 
  Serial.print("   ");

 // 라인트레이서 인식 세팅
  if (L == LOW && C == LOW && R == LOW ) {          // 0 0 0
    L = SL; C = SC; R = SR;
  }
 // 라인트레이서에서 센터만 인식이 됐을경우 직진,
  if (L == LOW && C == HIGH && R == LOW ) {         // 0 1 0
    motor_role(HIGH, HIGH);
    Serial.println("직진");
  }
  
  // 라인트레이서에서 오른쪽만 인식이 됐을경우 우회전,
  else if (L == LOW && R == HIGH ){                  // 0 0 1, 0 1 1
    motor_role(LOW, HIGH);
    Serial.println("우회전");
  }
 
  // 라인트레이서에서 왼쪽만 인식이 됏을 경우 좌회전,
  else if (L == HIGH && R == LOW ) {                 // 1 0 0, 1 1 0
    motor_role(HIGH, LOW);
    Serial.println("좌회전");
  }
  // 라인트레이서에서 왼쪽 오른쪽 전부 인식이 됐을경우, 정지
  else if (L == HIGH && R == HIGH ) {               // 1 1 1, 1 0 1
    analogWrite(RightMotor_E_pin, 0);
    analogWrite(LeftMotor_E_pin, 0);
    Serial.println("정지");
  }
  
  // 전방에 15cm 안에 물체가 감지됐을 경우 후진 후 정지,
  else if (Ultra_d < 150) {
      erial.println("150 이하.");
      motor_role(LOW, LOW);// 후진
      Serial.println("물체 감지! 정지 정지 정지");
      delay(1000);
      analogWrite(RightMotor_E_pin, 0);  
      analogWrite(LeftMotor_E_pin, 0);
      delay(200);
    }
  SL = L; SC = C; SR = R;
}
 // 디지털방식으로 모터의 출력 상태 0, 1로 기록
void motor_role(int R_motor, int L_motor) {
  digitalWrite(RightMotor_1_pin, R_motor);
  digitalWrite(RightMotor_2_pin, !R_motor);
  digitalWrite(LeftMotor_3_pin, L_motor);
  digitalWrite(LeftMotor_4_pin, !L_motor);
 // 아날로그 방식으로 모터의 출력 상태 0 ~ 255 기록
  analogWrite(RightMotor_E_pin, R_MotorSpeed); // 우측 모터 속도값 기록
  analogWrite(LeftMotor_E_pin, L_MotorSpeed);  // 좌측 모터 속도값 기록
}

 // 초음파 센서 작동
int Ultrasonic(){
  longduration, distance;
  digitalWrite(trigPin, HIGH);     // trigPin에서 초음파 발생       
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);  // echoPin 이 HIGH를 유지한 시간을 저장 한다.
  distance = ((float)(340* duration)/ 1000)/ 2; 
  //Serial.print("DIstance:");        // 물체와 초음파 센서간 거리를 표시.        
  //Serial.println(distance);
  returndistance;
}
 // 초음파 센서와 연결된 서보모터 작동
int Servo_con(){
  Servo.write(30);
  delay(300);
  intUlt_30 = Ultrasonic();
  delay(700);
  Servo.write(150);
  delay(300);
  intUlt_150 = Ultrasonic();
  delay(700);
  if(Ult_30 > Ult_150){
     val = 1;
  }
  else{
     val = 0;
  }
  Servo.write(90);
  
  returnval;
}

10. 트랙주행 소스코드 (최종)
#include <Servo.h>               // 서보 라이브러리
Servo Servo;
//출력핀(trig)과 입력핀(echo)
inttrigPin = 13;                 // 디지털 13번 핀에 연결
intechoPin = 12;                 // 디지털 12번 핀에 연결
intUltra_d = 0;                  // 초음파 센서
intval = 0;                   // 좌우 경로 설정 변수
   
intRightMotor_E_pin = 5;      // 오른쪽 모터 전원부 5번 연결핀
intLeftMotor_E_pin = 6;       // 왼쪽 모터 전원부 6번 연결핀
intRightMotor_1_pin = 10;      // 오른쪽 모터  8번 IN1
intRightMotor_2_pin = 11;      // 오른쪽 모터  9번 IN2
intLeftMotor_3_pin = 8;      // 왼쪽 모터  10번 IN3
intLeftMotor_4_pin = 9;      // 왼쪽 모터  11번 IN4
//모터 속도 조절, 최대속도 : 255
intL_MotorSpeed = 140;// 왼쪽 모터 속도
intR_MotorSpeed = 140;// 오른쪽 모터 속도
intL_Line = A5;// 왼쪽 라인트레이서 센서 - 확장쉴드 A5
intC_Line = A4;// 가운데 라인트레이서 센서 - 확장쉴드 A4
intR_Line = A3;// 오른쪽 라인트레이서 센서 - 확장쉴드 A3
//라인트레이서 적외선센서 값
intSL = 1;
intSC = 1;
intSR = 1;
 // 부품 셋업
void setup() {
  Servo.attach(2);                      // 서보모터 PWM 디지털입출력 2번핀 연결
  pinMode(echoPin, INPUT);                 // echoPin 입력
  pinMode(trigPin, OUTPUT);                // trigPin 출력
  // 모터 핀 설치
  pinMode(RightMotor_E_pin, OUTPUT);// 오른쪽 모터 전원부 출력
  pinMode(LeftMotor_E_pin, OUTPUT);// 왼쪽 모터 전원부 출력
  pinMode(RightMotor_1_pin, OUTPUT);// 오른쪽 모터 앞바퀴 출력
  pinMode(RightMotor_2_pin, OUTPUT);// 오른쪽 모터 뒷바퀴 출력
  pinMode(LeftMotor_3_pin, OUTPUT);// 왼쪽 모터 앞바퀴 출력
  pinMode(LeftMotor_4_pin, OUTPUT);// 왼쪽 모터 뒷바퀴 출력
  Serial.begin(9600);   // PC와의 시리얼 통신 값 9600
  Serial.println("Activate!");// 통신에 성공했을 경우, 시리얼 모니터 창에 Activate! 출력
}
 // 라인트레이서 값 읽기
void loop() {
  Ultra_d = Ultrasonic();// 초음파 센서
  Serial.println(Ultra_d);
  intL = digitalRead(L_Line);
  intC = digitalRead(C_Line);
  intR = digitalRead(R_Line);

  Serial.print("digital : "); 
  Serial.print(L); 
  Serial.print(", "); 
  Serial.print(C); 
  Serial.print(", "); 
  Serial.print(R); 
  Serial.print("   ");

 // 라인트레이서 인식 세팅
  if (L == LOW && C == LOW && R == LOW ) {
    L = SL; C = SC; R = SR;
  }
 // 라인트레이서에서 센터만 인식이 됐을경우 직진,
  if (L == LOW && C == HIGH && R == LOW ) {
    if (Ultra_d < 70 ) {// 물체가 70mm 앞에 감지됐을 경우,  장애물 감지및 위험회피 알고리즘 작동
      Serial.println("위험, 물체 감지!");
      analogWrite(RightMotor_E_pin, 0);  
      analogWrite(LeftMotor_E_pin, 0);
      delay(3000);
      motor_role(LOW, LOW);// 후진
      delay(1000);
      analogWrite(RightMotor_E_pin, 0);  
      analogWrite(LeftMotor_E_pin, 0);
      delay(1000);
      Servo.write(30);
      delay(1000);
      Servo.write(180);
      delay(1000);
      Servo.write(90);
      delay(5000);
      motor_role(HIGH, HIGH);
      delay(500);
    }   
    motor_role(HIGH, HIGH);
    Serial.println("직진");
  }
  
  // 라인트레이서에서 오른쪽만 인식이 됐을경우 우회전,
  else if (L == LOW && R == HIGH ){                  
    motor_role(LOW, HIGH);
    Serial.println("우회전");
  }
 
  // 라인트레이서에서 왼쪽만 인식이 됏을 경우 좌회전,
  else if (L == HIGH && R == LOW ) {                
    motor_role(HIGH, LOW);
    Serial.println("좌회전");
  }
  // 라인트레이서에서 왼쪽 오른쪽 전부 인식이 됐을경우, 정지
  else if (L == HIGH && R == HIGH ) {               
    analogWrite(RightMotor_E_pin, 0);
    analogWrite(LeftMotor_E_pin, 0);
    Serial.println("정지");
  }
  // 주차 감지 알고리즘
  if (Ultra_d < 130 ) {// 130mm 앞에 물체가 감지됐을 경우
    if (L == HIGH && C == HIGH && R == HIGH  ) {// 적외선 센서가 전부 켜져있을 경우
      Serial.println("주차 감지.");
      analogWrite(RightMotor_E_pin, 0);  
      analogWrite(LeftMotor_E_pin, 0);
      delay(3000);
      motor_role(LOW, LOW);// 후진
      delay(700);
      motor_role(HIGH, LOW);// 회전
      delay(800);
      motor_role(HIGH, HIGH);// 전진
      delay(500);
    }
  }
      
   SL = L; SC = C; SR = R;
}

 // 디지털방식으로 모터의 출력 상태 0, 1로 기록
void motor_role(int R_motor, int L_motor) {
  digitalWrite(RightMotor_1_pin, R_motor);
  digitalWrite(RightMotor_2_pin, !R_motor);
  digitalWrite(LeftMotor_3_pin, L_motor);
  digitalWrite(LeftMotor_4_pin, !L_motor);
 // 아날로그 방식으로 모터의 출력 상태 0 ~ 255 기록
  analogWrite(RightMotor_E_pin, R_MotorSpeed); // 우측 모터 속도값 기록
  analogWrite(LeftMotor_E_pin, L_MotorSpeed);  // 좌측 모터 속도값 기록
}

 // 초음파 센서 작동
int Ultrasonic(){
  longduration, distance;
  digitalWrite(trigPin, HIGH);     // trigPin에서 초음파 발생       
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);  // echoPin 이 HIGH를 유지한 시간 저장
  distance = ((float)(340* duration)/ 1000)/ 2; 
  returndistance;
}