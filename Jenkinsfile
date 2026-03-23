pipeline {
    agent any

    stages {

        stage('Stage 1 - Checkout Code') {
            steps {
                echo 'Checking out main branch...'
                checkout scm
                sh '''
                    git checkout main
                    git pull origin main
                '''
                echo '✅ 1st test is done'
            }
        }

        stage('Stage 2 - Run Python App') {
            steps {
                echo 'Running Python application...'
                sh 'python3 app.py'
                echo '✅ All tests are done'
            }
        }

        stage('Stage 3 - Send Output to Localhost Server') {
            steps {
                echo 'Sending output to localhost server...'
                sh '''
                    curl -X POST http://localhost:5000/jenkins-output \
                    -H "Content-Type: application/json" \
                    -d @output.json
                '''
            }
        }
    }

    post {
        always {
            echo 'Archiving artifacts...'
            archiveArtifacts artifacts: 'output.txt, output.html, output.json', fingerprint: true
        }
    }
}
