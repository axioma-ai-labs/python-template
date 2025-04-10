module.exports = {
    preset: 'angular',
    branches: [
      'main',
      'dev',
      { name: 'hotfix/*', prerelease: false }
    ],
    initialVersion: 'v0.0.0',
    tagFormat: 'v${version}',
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