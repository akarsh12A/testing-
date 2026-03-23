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

        stage('Stage 2 - Start Flask Server') {
            steps {
                echo 'Starting Flask server (if not already running)...'
                sh '''
                    if ! lsof -i:6000 >/dev/null 2>&1; then
                        echo "Flask server not running. Starting it..."
                        nohup python3 server.py > flask.log 2>&1 &
                        sleep 3
                    else
                        echo "Flask server already running."
                    fi
                '''
            }
        }

        stage('Stage 3 - Run Python App') {
            steps {
                echo 'Running Python application...'
                sh 'python3 sample.py'
                echo '✅ All tests are done'
            }
        }

        stage('Stage 4 - Send Output to Localhost Server') {
            steps {
                echo 'Sending output to localhost server...'
                sh '''
                    curl -X POST http://localhost:6000/jenkins-output \
                    -H "Content-Type: application/json" \
                    -d @output.json \
                    || echo "⚠️ Flask server not reachable, skipping send"
                '''
            }
        }
    }

    post {
        always {
            echo 'Archiving artifacts...'
            archiveArtifacts artifacts: 'output.txt, output.html, output.json, flask.log', fingerprint: true
        }
    }
}
