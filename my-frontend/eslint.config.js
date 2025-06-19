/**
 * ESLint configuration for the project:
 * - Ignores the 'dist' directory.
 * - Targets all .js and .jsx files.
 * - Uses ECMAScript 2020 syntax and module source type with JSX support.
 * - Enables browser global variables.
 * - Registers the react-hooks and react-refresh plugins.
 * - Extends recommended rules from @eslint/js and react-hooks.
 * - Customizes 'no-unused-vars' to ignore identifiers starting with uppercase letters or underscores.
 * - Warns on react-refresh export rules, allowing constant exports.
 */

import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'

export default [
  { ignores: ['dist'] },
  {
    files: ['**/*.{js,jsx}'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
      parserOptions: {
        ecmaVersion: 'latest',
        ecmaFeatures: { jsx: true },
        sourceType: 'module',
      },
    },
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
    },
    rules: {
      ...js.configs.recommended.rules,
      ...reactHooks.configs.recommended.rules,
      'no-unused-vars': ['error', { varsIgnorePattern: '^[A-Z_]' }],
      'react-refresh/only-export-components': [
        'warn',
        { allowConstantExport: true },
      ],
    },
  },
]
