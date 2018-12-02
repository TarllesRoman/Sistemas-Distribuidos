#include <aJSON.h>
#include <SoftwareSerial.h>
#include <Servo.h>

#define SERVO 2//define motor servo na porta digital 6
#define REL 10//define rele de energia na porta digital 7
#define ESQ 130 //define alimentador saida da esquerda
#define DIR 15 // define alimentador saida da direita
#define CEN 70 // define alimentador centro
#define DELPOS 500//Define um delay de giro de posicao do servo

SoftwareSerial BT(5, 7); // RX, TX
Servo s;//variavel do tipo servo
char cmd;

String command = ""; // Stores response of bluetooth device

void setup()
{
  Serial.begin(9600);
  Serial.println("Type AT commands!");
  BT.begin(9600); // HC-06 usually default baud-rate
  pinMode(SERVO, OUTPUT);
  pinMode(REL,OUTPUT);
  digitalWrite(REL, HIGH);//Desliga rele alimentador
  s.attach(SERVO);
}

void loop()
{
  if (BT.available()) {
    while(BT.available()){
     delay(10);
     char c = BT.read();
     command += c;
    }
    Serial.println(command);
    char jj[100];
    command.toCharArray(jj, 100);
    aJsonObject* root = aJson.parse(jj);
    aJsonObject* tempo = aJson.getObjectItem(root, "tempo");
    Serial.println("TEMPO: ");
    Serial.println(tempo->valueint);
    aJsonObject* tanque = aJson.getObjectItem(root, "tanque");
    Serial.println("TANQUE");
    Serial.print(tanque->valueint);
    
    if(tanque->valueint==1){
      Serial.write("Tanque1");
      servoDir();
      alimentar(tempo->valueint);
      servoZero();
    }
    
    if(tanque->valueint==2){
      Serial.write("Tanque2");
      servoCentro();
      alimentar(tempo->valueint);
      servoZero();
    }
    
    if(tanque->valueint==3){
      Serial.write("Tanque3");
      servoEsq();
      alimentar(tempo->valueint);
      servoZero(); 
    }
    long siz = 4;
    BT.print(String("End!"));
    command = ""; 
  }
}



/***************************************
 * Ativa rele para alimentação de peixes
 */
void releLigado(int tempAlim){
  digitalWrite(REL, LOW);//Liga rele alimentador
  delay(tempAlim);//Define tempo que alimentador fica ligado
}//fim releligado **************************************


/****************************************
 * Ativa rele para alimentação de peixes
 */
void releDesligado(){
  digitalWrite(REL, HIGH);//Desliga rele alimentador
}//fim reledesligado**************************************


/****************************************
 * posiciona o alimentador no centro
 */
void servoCentro(){
    s.write(0);
    delay(DELPOS);
    s.write(CEN);
}//fim servo centro**************************************


/****************************************
 * posiciona o alimentador na esquerda do servo
 */
void servoEsq(){
    s.write(0);
    delay(DELPOS);
    s.write(ESQ);
}// fim servoesq**************************************


/****************************************
 * posiciona o alimentador na direita do servo
 */
void servoDir(){
    s.write(0);
    delay(DELPOS);
    s.write(DIR);
}// fim servodir**************************************

/****************************************
 * posiciona o alimentador na posicao 0
 */
void servoZero(){
    s.write(0);
}// fim servodir**************************************


/****************************************
 * define a quantidde em gramas que se deve alimentar no momento
 */
void alimentar(int tempo){
  //float tempo = (qtdG/130)*RAC10G;divide a quantidade por 10 pois o tempo min de alim e 10G
  releLigado(tempo);
  releDesligado();
}//fim alimentar**************************************


