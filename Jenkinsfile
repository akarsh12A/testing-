pipeline {
    agent any

    stages {
        stage('Run Python Script') {
            steps {
                echo 'Running Python file...'
                sh 'python3 sample.py'
            }
        }
    }

    post {
        success {
            echo '✅ Jenkins job SUCCESS'
        }
        failure {
            echo '❌ Jenkins job FAILED'
        }
        always {
            archiveArtifacts artifacts: 'output.txt, output.html, output.json', fingerprint: true
            echo 'Artifacts archived'
        }
    }
}
