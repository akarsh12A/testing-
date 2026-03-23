pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 app.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'output.txt, output.html', fingerprint: true
        }
    }
}


