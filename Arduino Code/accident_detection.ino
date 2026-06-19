#define MQ3 A0

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int gas = analogRead(MQ3);

  float x = random(0,300)/100.0;
  float y = random(0,300)/100.0;

  Serial.print(gas);
  Serial.print(",");
  Serial.print(x);
  Serial.print(",");
  Serial.println(y);

  delay(1000);
}