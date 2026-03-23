pipeline {
    agent any

    stages {

        stage('Stage 1 - Checkout and Pull') {
            steps {
                echo 'Checking out main branch...'

                // Checkout repository
                checkout scm

                // Ensure we are on main branch and pull latest changes
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

                sh 'python3 sample.py'

                echo '✅ All tests are done'
            }
    }
}

post {
        always {
            echo 'Archiving build artifacts...'

            archiveArtifacts artifacts: 'output.html, output.txt', fingerprint: true
        }
    }


}
