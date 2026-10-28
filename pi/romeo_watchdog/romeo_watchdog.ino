
const int LEFT_DIR = 4;
const int LEFT_PWM = 5;
const int RIGHT_PWM = 6;
const int RIGHT_DIR = 7;

const unsigned long TIMEOUT_MS = 500;
unsigned long lastCommand = 0;

void stopMotors() {
    analogWrite(LEFT_PWM, 0);
    analogWrite(RIGHT_PWM, 0);
}

// Positive speed = forwards
// Negative speed = backwards
void drive(int left, int right) {
    // Disable motor outputs before changing directions
    analogWrite(LEFT_PWM, 0);
    analogWrite(RIGHT_PWM, 0);

    // Directions verified on your robot
    digitalWrite(LEFT_DIR, left >= 0 ? HIGH : LOW);
    digitalWrite(RIGHT_DIR, right >= 0 ? LOW : HIGH);

    analogWrite(LEFT_PWM, abs(left));
    analogWrite(RIGHT_PWM, abs(right));
}

void setup() {
    pinMode(LEFT_DIR, OUTPUT);
    pinMode(LEFT_PWM, OUTPUT);
    pinMode(RIGHT_DIR, OUTPUT);
    pinMode(RIGHT_PWM, OUTPUT);

    stopMotors();

    Serial.begin(9600);
    lastCommand = millis();
}

void loop() {
    while (Serial.available() > 0) {
        char command = Serial.read();
        bool valid = true;

        switch (command) {
    case 'F': drive(200, 170); break;
    case 'B': drive(-160, -170); break;

    // Turn on the spot
    case 'L': drive(200, -200); break;
    case 'R': drive(-200, 200); break;

    // Steer while moving forwards
    case 'G': drive(200, 80); break;
    case 'H': drive(80, 200); break;

    // Steer while moving backwards
    case 'J': drive(-200, -80); break;
    case 'K': drive(-80, -200); break;

    case 'X': stopMotors(); break;

    default:
        stopMotors();
        valid = false;
        break;
}

        if (valid) {
            lastCommand = millis();
        }
    }

    // Stop if communication stops
    if (millis() - lastCommand > TIMEOUT_MS) {
        stopMotors();
    }
}
