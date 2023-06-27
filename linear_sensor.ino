int sensorPin = A0;

void setup() {
  Serial.begin(115200);
  pinMode(sensorPin, INPUT);
}

void loop() {
  int value = analogRead(sensorPin);
  Serial.println(value);
  delay(10);
}