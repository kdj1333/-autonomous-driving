#include <IRremote.h>
int RECV_PIN = A0;              // 적외선 수신센서 핀(아날로그 입력 A0)
IRrecv irrecv(RECV_PIN);        // 적외선 송수신 통신을 위한 객체
decode_results IR_Signal;       // 적외선 수신값 해석을 위한 객체

int RightMotor_E_pin = 5;       // 오른쪽 모터의 Enable & PWM
int LeftMotor_E_pin = 6;        // 왼쪽 모터의 Enable & PWM
int RightMotor_1_pin = 8;       // 오른쪽 모터 제어선 IN1
int RightMotor_2_pin = 9;       // 오른쪽 모터 제어선 IN2
int LeftMotor_3_pin = 10;       // 왼쪽 모터 제어선 IN3
int LeftMotor_4_pin = 11;       // 왼쪽 모터 제어선 IN4

int motor_s = 153;              // 최대 속도(0~255)의 60% 

int R_Motor = 0;
int L_Motor = 0;
int mode = 0;

void setup() {
  pinMode(RightMotor_E_pin, OUTPUT);        // 출력모드로 설정
  pinMode(RightMotor_1_pin, OUTPUT);
  pinMode(RightMotor_2_pin, OUTPUT);
  pinMode(LeftMotor_3_pin, OUTPUT);
  pinMode(LeftMotor_4_pin, OUTPUT);
  pinMode(LeftMotor_E_pin, OUTPUT);

  Serial.begin(9600);                       // PC와의 시리얼 통신 9600bps로 설정
  Serial.println("Welcome Eduino!");
  
  irrecv.enableIRIn(); // 적외선 통신 수신 시작
}

void loop() { 
  if(irrecv.decode(&IR_Signal)){      // 적외선(IR) 수신값이 있는지 판단.       

    Serial.print("Input Signal : ");
    Serial.print("HEX[ "); Serial.print(IR_Signal.value, HEX); Serial.print(" ], ");
    Serial.print("Int[ "); Serial.print((String)IR_Signal.value); Serial.print(" ] || ");
    
    control_SmartCar((String)IR_Signal.value);

    if(mode == 0){
      motor_role(R_Motor, L_Motor, motor_s);
    }
    else if(mode == 1){
      Right_role(R_Motor, L_Motor, motor_s);
    }
    else if(mode == 2){
      Left_role(R_Motor, L_Motor, motor_s);
    }
    else{
      motor_role(R_Motor, L_Motor, 0);
    }
    
    irrecv.resume();  // 다음 적외선 값 수신   
  } 
}

void control_SmartCar(String Remote_Val){ 
  if( Remote_Val == "16754775" ){      // "+" 버튼, 명령 : 속도 증가
    motor_s = motor_s + 20;
    motor_s = min(motor_s, 255);
    Serial.print("Speed Up : "); 
  }
  
  else if( Remote_Val == "16769055" ){ // "-" 버튼, 명령 : 속도 감소
    motor_s = motor_s - 20;
    motor_s = max(motor_s, 50);
    Serial.print("Speed Down : ");
  }
  
  else if(Remote_Val == "16718055" ){  // "2" 버튼, 명령 : 전진
    R_Motor = HIGH; L_Motor = HIGH; mode = 0;
    Serial.print("Forward : ");
  }  
  
  else if( Remote_Val == "16716015" ){ // "4" 버튼, 명령 : 좌회전
    mode = 2;
    Serial.print("Turn Left : "); 
  }
  
  else if( Remote_Val == "16734885" ){ // "6" 버튼, 명령 : 우회전
    mode = 1;
    Serial.print("Turn Right : "); 
  }
  
  else if( Remote_Val == "16730805" ){ // "8" 버튼, 명령 : 후진
    R_Motor = LOW; L_Motor = LOW; mode = 0;
    Serial.print("Backward : "); 
  }

  else if( Remote_Val == "16726215" ){ // "5" 버튼, 명령 : 정지
    mode = 3;
    Serial.print("Stop : ");  
  }
  
  else{
    Serial.print("Not Defined : ");  // 지정하지 않은 주소입력.
  }
  
  Serial.print("R_Motor[ ");Serial.print(R_Motor);Serial.print(" ], ");
  Serial.print("L_Motor[ ");Serial.print(L_Motor);Serial.print(" ], ");
  Serial.print("motor_s[ ");Serial.print(motor_s);Serial.print(" ], ");
  Serial.print("Mode[ ");Serial.print(mode);Serial.println(" ]");
}

void motor_role(int R_motor, int L_motor, int Speed){
   digitalWrite(RightMotor_1_pin, R_motor);
   digitalWrite(RightMotor_2_pin, !R_motor);
   digitalWrite(LeftMotor_3_pin, L_motor);
   digitalWrite(LeftMotor_4_pin, !L_motor);
   
   analogWrite(RightMotor_E_pin, Speed);  // 우측 모터 속도값
   analogWrite(LeftMotor_E_pin, Speed);   // 좌측 모터 속도값  
}

void Right_role(int R_motor, int L_motor, int Speed){
   digitalWrite(RightMotor_1_pin, R_motor);
   digitalWrite(RightMotor_2_pin, !R_motor);
   digitalWrite(LeftMotor_3_pin, L_motor);
   digitalWrite(LeftMotor_4_pin, !L_motor);
   
   analogWrite(RightMotor_E_pin, max(Speed*0.4,50));  // 우측 모터 속도값
   analogWrite(LeftMotor_E_pin, min(Speed*1.4,255));   // 좌측 모터 속도값
}

void Left_role(int R_motor, int L_motor, int Speed){
   digitalWrite(RightMotor_1_pin, R_motor);
   digitalWrite(RightMotor_2_pin, !R_motor);
   digitalWrite(LeftMotor_3_pin, L_motor);
   digitalWrite(LeftMotor_4_pin, !L_motor);
   
   analogWrite(RightMotor_E_pin, min(Speed*1.4,255));  // 우측 모터 속도값
   analogWrite(LeftMotor_E_pin, max(Speed*0.2,50));   // 좌측 모터 속도값   
}
