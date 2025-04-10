module.exports = {
    // Define the branches for release.
    branches: [
      { name: 'main' },
      { name: 'dev', channel: 'dev', prerelease: false }
    ],
    // Map commit types to releases.
    // Breaks any commit that normally triggers a major bump so that only minor or patch releases occur.
    releaseRules: [
      { type: 'major', release: 'patch' }, // Force breaking changes to become patch releases.
      { type: 'minor', release: 'minor' },
      { type: 'patch', release: 'patch' },
      { type: 'fix', release: 'patch' }
    ],
    // Change the tag format. This enforces a 0.x.x version.
    tagFormat: '0.${version}',
    // List the plugins to use during the release process.
    plugins: [
      // Analyze commits for changes.
      '@semantic-release/commit-analyzer',
      // Generate a changelog.
      '@semantic-release/release-notes-generator',
      // Create and publish a new GitHub release.
      '@semantic-release/github'
    ]
  };