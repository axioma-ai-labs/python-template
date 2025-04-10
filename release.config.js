module.exports = {
    preset: 'angular',
    branches: [
      { name: 'main' },
      { name: 'dev', channel: 'dev', prerelease: false }
    ],
    releaseRules: [
      { type: 'major', release: 'patch' }, 
      { type: 'feat', release: 'minor' },
      { type: 'fix', release: 'patch' },
      { type: 'perf', release: 'patch' }
    ],
    tagFormat: '0.${version}',
    plugins: [
      '@semantic-release/commit-analyzer',
      '@semantic-release/release-notes-generator',
      '@semantic-release/github'
    ]
  };