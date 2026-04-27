// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

package cmd

import (
	"context"
	"fmt"

	"github.com/Ramensoft/handinger-cli/internal/apiquery"
	"github.com/Ramensoft/handinger-cli/internal/requestflag"
	"github.com/Ramensoft/handinger-go"
	"github.com/Ramensoft/handinger-go/option"
	"github.com/tidwall/gjson"
	"github.com/urfave/cli/v3"
)

var workersCreate = cli.Command{
	Name:    "create",
	Usage:   "Create a new agent worker and start it with the supplied instruction. Send\n`multipart/form-data` to attach files alongside the instruction; the bytes are\nbootstrapped into the worker's workspace before the first turn.",
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
	Usage:   "Retrieve the current worker state and messages. Returns a JSON worker object by\ndefault, or a server-sent event stream when `stream=true`.",
	Suggest: true,
	Flags: []cli.Flag{
		&requestflag.Flag[string]{
			Name:     "worker-id",
			Required: true,
		},
		&requestflag.Flag[string]{
			Name:      "stream",
			Usage:     `Set to "true" to receive a server-sent event stream that replays all stored messages and then continues with live chunks from the active turn (if any) before closing.`,
			QueryPath: "stream",
		},
	},
	Action:          handleWorkersRetrieve,
	HideHelpCommand: true,
}

var workersContinue = cli.Command{
	Name:    "continue",
	Usage:   "Send another instruction to an existing worker. Send `multipart/form-data` to\nattach additional files; the bytes are bootstrapped into the worker's workspace\nbefore the next turn.",
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

	params := handinger.WorkerGetParams{}

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
	_, err = client.Workers.Get(
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
