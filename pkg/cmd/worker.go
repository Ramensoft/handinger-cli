// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

package cmd

import (
	"context"
	"fmt"
	"os"

	"github.com/Ramensoft/handinger-cli/internal/apiquery"
	"github.com/Ramensoft/handinger-cli/internal/requestflag"
	"github.com/Ramensoft/handinger-go"
	"github.com/Ramensoft/handinger-go/option"
	"github.com/tidwall/gjson"
	"github.com/urfave/cli/v3"
)

var workersCreate = cli.Command{
	Name:    "create",
	Usage:   "Create a new agent worker and start it with the supplied instruction.",
	Suggest: true,
	Flags: []cli.Flag{
		&requestflag.Flag[string]{
			Name:     "input",
			Required: true,
			BodyPath: "input",
		},
		&requestflag.Flag[string]{
			Name:     "budget",
			Usage:    `Allowed values: "low", "standard", "high", "unlimited".`,
			Default:  "standard",
			BodyPath: "budget",
		},
		&requestflag.Flag[bool]{
			Name:     "stream",
			Default:  false,
			BodyPath: "stream",
		},
	},
	Action:          handleWorkersCreate,
	HideHelpCommand: true,
}

var workersRetrieve = cli.Command{
	Name:    "retrieve",
	Usage:   "Retrieve the current worker state and messages.",
	Suggest: true,
	Flags: []cli.Flag{
		&requestflag.Flag[string]{
			Name:     "worker-id",
			Required: true,
		},
	},
	Action:          handleWorkersRetrieve,
	HideHelpCommand: true,
}

var workersContinue = cli.Command{
	Name:    "continue",
	Usage:   "Send another instruction to an existing worker.",
	Suggest: true,
	Flags: []cli.Flag{
		&requestflag.Flag[string]{
			Name:     "worker-id",
			Required: true,
		},
		&requestflag.Flag[string]{
			Name:     "input",
			Required: true,
			BodyPath: "input",
		},
		&requestflag.Flag[string]{
			Name:     "budget",
			Usage:    `Allowed values: "low", "standard", "high", "unlimited".`,
			Default:  "standard",
			BodyPath: "budget",
		},
		&requestflag.Flag[bool]{
			Name:     "stream",
			Default:  false,
			BodyPath: "stream",
		},
	},
	Action:          handleWorkersContinue,
	HideHelpCommand: true,
}

var workersRetrieveEmail = cli.Command{
	Name:    "retrieve-email",
	Usage:   "Retrieve the inbound email address for a worker.",
	Suggest: true,
	Flags: []cli.Flag{
		&requestflag.Flag[string]{
			Name:     "worker-id",
			Required: true,
		},
	},
	Action:          handleWorkersRetrieveEmail,
	HideHelpCommand: true,
}

var workersRetrieveFile = cli.Command{
	Name:    "retrieve-file",
	Usage:   "Retrieve a file published from a worker workspace. The runtime route accepts\nnested paths after /files/.",
	Suggest: true,
	Flags: []cli.Flag{
		&requestflag.Flag[string]{
			Name:     "worker-id",
			Required: true,
		},
		&requestflag.Flag[string]{
			Name:     "file-path",
			Required: true,
		},
		&requestflag.Flag[string]{
			Name:    "output",
			Aliases: []string{"o"},
			Usage:   "The file where the response contents will be stored. Use the value '-' to force output to stdout.",
		},
	},
	Action:          handleWorkersRetrieveFile,
	HideHelpCommand: true,
}

func handleWorkersCreate(ctx context.Context, cmd *cli.Command) error {
	client := handinger.NewClient(getDefaultRequestOptions(cmd)...)
	unusedArgs := cmd.Args().Slice()

	if len(unusedArgs) > 0 {
		return fmt.Errorf("Unexpected extra arguments: %v", unusedArgs)
	}

	params := handinger.WorkerNewParams{}

	options, err := flagOptions(
		cmd,
		apiquery.NestedQueryFormatBrackets,
		apiquery.ArrayQueryFormatComma,
		ApplicationJSON,
		false,
	)
	if err != nil {
		return err
	}

	var res []byte
	options = append(options, option.WithResponseBodyInto(&res))
	_, err = client.Workers.New(ctx, params, options...)
	if err != nil {
		return err
	}

	obj := gjson.ParseBytes(res)
	format := cmd.Root().String("format")
	explicitFormat := cmd.Root().IsSet("format")
	transform := cmd.Root().String("transform")
	return ShowJSON(obj, ShowJSONOpts{
		ExplicitFormat: explicitFormat,
		Format:         format,
		RawOutput:      cmd.Root().Bool("raw-output"),
		Title:          "workers create",
		Transform:      transform,
	})
}

func handleWorkersRetrieve(ctx context.Context, cmd *cli.Command) error {
	client := handinger.NewClient(getDefaultRequestOptions(cmd)...)
	unusedArgs := cmd.Args().Slice()
	if !cmd.IsSet("worker-id") && len(unusedArgs) > 0 {
		cmd.Set("worker-id", unusedArgs[0])
		unusedArgs = unusedArgs[1:]
	}
	if len(unusedArgs) > 0 {
		return fmt.Errorf("Unexpected extra arguments: %v", unusedArgs)
	}

	options, err := flagOptions(
		cmd,
		apiquery.NestedQueryFormatBrackets,
		apiquery.ArrayQueryFormatComma,
		EmptyBody,
		false,
	)
	if err != nil {
		return err
	}

	var res []byte
	options = append(options, option.WithResponseBodyInto(&res))
	_, err = client.Workers.Get(ctx, cmd.Value("worker-id").(string), options...)
	if err != nil {
		return err
	}

	obj := gjson.ParseBytes(res)
	format := cmd.Root().String("format")
	explicitFormat := cmd.Root().IsSet("format")
	transform := cmd.Root().String("transform")
	return ShowJSON(obj, ShowJSONOpts{
		ExplicitFormat: explicitFormat,
		Format:         format,
		RawOutput:      cmd.Root().Bool("raw-output"),
		Title:          "workers retrieve",
		Transform:      transform,
	})
}

func handleWorkersContinue(ctx context.Context, cmd *cli.Command) error {
	client := handinger.NewClient(getDefaultRequestOptions(cmd)...)
	unusedArgs := cmd.Args().Slice()
	if !cmd.IsSet("worker-id") && len(unusedArgs) > 0 {
		cmd.Set("worker-id", unusedArgs[0])
		unusedArgs = unusedArgs[1:]
	}
	if len(unusedArgs) > 0 {
		return fmt.Errorf("Unexpected extra arguments: %v", unusedArgs)
	}

	params := handinger.WorkerContinueParams{}

	options, err := flagOptions(
		cmd,
		apiquery.NestedQueryFormatBrackets,
		apiquery.ArrayQueryFormatComma,
		ApplicationJSON,
		false,
	)
	if err != nil {
		return err
	}

	var res []byte
	options = append(options, option.WithResponseBodyInto(&res))
	_, err = client.Workers.Continue(
		ctx,
		cmd.Value("worker-id").(string),
		params,
		options...,
	)
	if err != nil {
		return err
	}

	obj := gjson.ParseBytes(res)
	format := cmd.Root().String("format")
	explicitFormat := cmd.Root().IsSet("format")
	transform := cmd.Root().String("transform")
	return ShowJSON(obj, ShowJSONOpts{
		ExplicitFormat: explicitFormat,
		Format:         format,
		RawOutput:      cmd.Root().Bool("raw-output"),
		Title:          "workers continue",
		Transform:      transform,
	})
}

func handleWorkersRetrieveEmail(ctx context.Context, cmd *cli.Command) error {
	client := handinger.NewClient(getDefaultRequestOptions(cmd)...)
	unusedArgs := cmd.Args().Slice()
	if !cmd.IsSet("worker-id") && len(unusedArgs) > 0 {
		cmd.Set("worker-id", unusedArgs[0])
		unusedArgs = unusedArgs[1:]
	}
	if len(unusedArgs) > 0 {
		return fmt.Errorf("Unexpected extra arguments: %v", unusedArgs)
	}

	options, err := flagOptions(
		cmd,
		apiquery.NestedQueryFormatBrackets,
		apiquery.ArrayQueryFormatComma,
		EmptyBody,
		false,
	)
	if err != nil {
		return err
	}

	var res []byte
	options = append(options, option.WithResponseBodyInto(&res))
	_, err = client.Workers.GetEmail(ctx, cmd.Value("worker-id").(string), options...)
	if err != nil {
		return err
	}

	obj := gjson.ParseBytes(res)
	format := cmd.Root().String("format")
	explicitFormat := cmd.Root().IsSet("format")
	transform := cmd.Root().String("transform")
	return ShowJSON(obj, ShowJSONOpts{
		ExplicitFormat: explicitFormat,
		Format:         format,
		RawOutput:      cmd.Root().Bool("raw-output"),
		Title:          "workers retrieve-email",
		Transform:      transform,
	})
}

func handleWorkersRetrieveFile(ctx context.Context, cmd *cli.Command) error {
	client := handinger.NewClient(getDefaultRequestOptions(cmd)...)
	unusedArgs := cmd.Args().Slice()
	if !cmd.IsSet("file-path") && len(unusedArgs) > 0 {
		cmd.Set("file-path", unusedArgs[0])
		unusedArgs = unusedArgs[1:]
	}
	if len(unusedArgs) > 0 {
		return fmt.Errorf("Unexpected extra arguments: %v", unusedArgs)
	}

	params := handinger.WorkerGetFileParams{
		WorkerID: cmd.Value("worker-id").(string),
	}

	options, err := flagOptions(
		cmd,
		apiquery.NestedQueryFormatBrackets,
		apiquery.ArrayQueryFormatComma,
		EmptyBody,
		false,
	)
	if err != nil {
		return err
	}

	response, err := client.Workers.GetFile(
		ctx,
		cmd.Value("file-path").(string),
		params,
		options...,
	)
	if err != nil {
		return err
	}
	message, err := writeBinaryResponse(response, os.Stdout, cmd.String("output"))
	if message != "" {
		fmt.Println(message)
	}
	return err
}
