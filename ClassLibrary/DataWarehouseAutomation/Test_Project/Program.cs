﻿using System;
using System.Collections.Generic;
using DataWarehouseAutomation;

namespace Test_Project
{
    class Program
    {
        static void Main(string[] args)
        {
            string jsonSchema = AppDomain.CurrentDomain.BaseDirectory + @"..\..\..\..\..\..\GenericInterface\interfaceDataWarehouseAutomationMetadata.json";

            var sampleTemplateDirectory = AppDomain.CurrentDomain.BaseDirectory + @"..\..\..\..\Sample_Metadata\";

            List<string> fileList = new List<string>();
            fileList.Add(sampleTemplateDirectory + @"sampleBasic.json"); // Most basic test
            fileList.Add(sampleTemplateDirectory + @"sampleBasicWithExtensions.json");
            fileList.Add(sampleTemplateDirectory + @"sampleMultipleDataItemMappings.json");
            fileList.Add(sampleTemplateDirectory + @"sampleSourceQuery.json"); // Simple test using a query as source
            fileList.Add(sampleTemplateDirectory + @"sampleCalculation.json"); // Simple test using one of the column mappings as calculation
            fileList.Add(sampleTemplateDirectory + @"sampleSimpleDDL.json"); // Simple test using one of the column mappings as calculation
            fileList.Add(sampleTemplateDirectory + @"sampleTEAM_Hub.json"); // Validating a Json generated by TEAM / VDW
            fileList.Add(sampleTemplateDirectory + @"sampleTEAM_Hub_v161.json"); // Validating a Json generated by TEAM / VDW
            fileList.Add(sampleTemplateDirectory + @"sampleTEAM_LSAT.json"); // Validating a Json generated by TEAM / VDW
            fileList.Add(sampleTemplateDirectory + @"sampleVDW_Hub.json"); // Validating a Json generated by TEAM / VDW
            fileList.Add(sampleTemplateDirectory + @"sampleVDW_StagingArea.json"); // Validating a Json generated by TEAM / VDW
            fileList.Add(sampleTemplateDirectory + @"sampleVDW_HubWithLookup.json"); // Validating a Json generated by TEAM / VDW
            fileList.Add(sampleTemplateDirectory + @"sampleTEAMv16.json"); // Validating a Json generated by TEAM / VDW
            fileList.Add(sampleTemplateDirectory + @"sampleJsonStagingWithPsaDetails.json"); // Validating a Json generated by TEAM / VDW            

            foreach (string jsonFile in fileList)
            {
                var result = JsonHandling.ValidateJsonFileAgainstSchema(jsonSchema, jsonFile);

                var testOutput = result.Valid ? "OK" : "Failed";

                Console.Write($"The result for {jsonFile} was {testOutput}.");
                foreach (var error in result.Errors)
                {
                    Console.Write($"   {error.Message} at line {error.LineNumber} position {error.LinePosition} of error type {error.ErrorType}. This is related to {error.Path}.");
                }
                Console.WriteLine();
                Console.WriteLine();
            }

            // Finish the application
            Console.ReadKey();
        }
    }
}
