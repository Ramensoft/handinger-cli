// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

package cmd

import (
	"testing"

	"github.com/Ramensoft/handinger-cli/internal/mocktest"
)

func TestWorkersCreate(t *testing.T) {
	t.Skip("Mock server tests are disabled")
	t.Run("regular flags", func(t *testing.T) {
		mocktest.TestRunMockTestWithFlags(
			t,
			"--api-key", "string",
			"workers", "create",
			"--input", "What's the weather today in Barcelona?",
			"--budget", "low",
			"--stream=true",
		)
	})

	t.Run("piping data", func(t *testing.T) {
		// Test piping YAML data over stdin
		pipeData := []byte("" +
			"input: What's the weather today in Barcelona?\n" +
			"budget: low\n" +
			"stream: true\n")
		mocktest.TestRunMockTestWithPipeAndFlags(
			t, pipeData,
			"--api-key", "string",
			"workers", "create",
		)
	})
}

func TestWorkersRetrieve(t *testing.T) {
	t.Skip("Mock server tests are disabled")
	t.Run("regular flags", func(t *testing.T) {
		mocktest.TestRunMockTestWithFlags(
			t,
			"--api-key", "string",
			"workers", "retrieve",
			"--worker-id", "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
			"--stream=true",
		)
	})
}

func TestWorkersContinue(t *testing.T) {
	t.Skip("Mock server tests are disabled")
	t.Run("regular flags", func(t *testing.T) {
		mocktest.TestRunMockTestWithFlags(
			t,
			"--api-key", "string",
			"workers", "continue",
			"--worker-id", "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
			"--input", "What's the weather today in Barcelona?",
			"--budget", "low",
			"--stream=true",
		)
	})

	t.Run("piping data", func(t *testing.T) {
		// Test piping YAML data over stdin
		pipeData := []byte("" +
			"input: What's the weather today in Barcelona?\n" +
			"budget: low\n" +
			"stream: true\n")
		mocktest.TestRunMockTestWithPipeAndFlags(
			t, pipeData,
			"--api-key", "string",
			"workers", "continue",
			"--worker-id", "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
		)
	})
}

func TestWorkersRetrieveEmail(t *testing.T) {
	t.Skip("Mock server tests are disabled")
	t.Run("regular flags", func(t *testing.T) {
		mocktest.TestRunMockTestWithFlags(
			t,
			"--api-key", "string",
			"workers", "retrieve-email",
			"--worker-id", "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
		)
	})
}

func TestWorkersRetrieveFile(t *testing.T) {
	t.Skip("Mock server tests are disabled")
	t.Run("regular flags", func(t *testing.T) {
		mocktest.TestRunMockTestWithFlags(
			t,
			"--api-key", "string",
			"workers", "retrieve-file",
			"--worker-id", "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
			"--file-path", "scratchpad/plan.md",
			"--output", "/dev/null",
		)
	})
}

func TestWorkersStreamUpdates(t *testing.T) {
	t.Skip("Mock server tests are disabled")
	t.Run("regular flags", func(t *testing.T) {
		mocktest.TestRunMockTestWithFlags(
			t,
			"--api-key", "string",
			"workers", "stream-updates",
			"--max-items", "10",
			"--worker-id", "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
		)
	})
}
