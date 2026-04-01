pipeline {
    agent any

    environment {
        SONAR_PROJECT_KEY  = "akarsh-python-project"
        SONAR_PROJECT_NAME = "Akarsh Python Sonar Project"
        VENV_DIR = "venv"
    }

    stages {

        stage('Set Up Python Virtual Environment') {
            steps {
                sh '''
                python3 --version
                python3 -m venv $VENV_DIR
                . $VENV_DIR/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . $VENV_DIR/bin/activate
                if [ -f requirements.txt ]; then
                    pip install -r requirements.txt
                fi
                '''
            }
        }

        stage('Run SonarQube Scan') {
            steps {
                withSonarQubeEnv('SonarQube-Server') {
                    sh '''
                    sonar-scanner \
                      -Dsonar.projectKey=$SONAR_PROJECT_KEY \
                      -Dsonar.projectName="$SONAR_PROJECT_NAME" \
                      -Dsonar.sources=. \
                      -Dsonar.python.version=3
                    '''
                }
            }
        }
    }
}
