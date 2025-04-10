module.exports = {
    preset: 'angular',
    branches: [
      { name: 'main' },
      { name: 'dev', channel: 'dev', prerelease: false }
    ],
    initialVersion: '0.1.0',
    tagFormat: '${version}',
    releaseRules: [
      { type: 'major', release: 'patch' },
      { type: 'feat', release: 'minor' },
      { type: 'fix', release: 'patch' },
      { type: 'perf', release: 'patch' }
    ],
    plugins: [
      '@semantic-release/commit-analyzer',
      '@semantic-release/release-notes-generator',
      '@semantic-release/github'
    ]
  };