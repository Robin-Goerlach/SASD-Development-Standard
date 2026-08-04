using Sasd.PromptManager.Application.PromptPackages;
using Sasd.PromptManager.Domain.Prompts;

namespace Sasd.PromptManager.Domain.Tests.PromptPackages;

public sealed class SasdPromptPackageImportMappingTests
{
    [Theory]
    [InlineData("architecture", PromptType.Architecture)]
    [InlineData("development", PromptType.Coding)]
    [InlineData("debugging", PromptType.Debugging)]
    [InlineData("documentation", PromptType.Documentation)]
    [InlineData("review", PromptType.Review)]
    [InlineData("requirements", PromptType.General)]
    public void MapPromptType_UsesProportionalExistingDomainTypes(string category, PromptType expected)
        => Assert.Equal(expected, SasdPromptPackageImportService.MapPromptType(category));

    [Theory]
    [InlineData("Stable", PromptStatus.Active)]
    [InlineData("Candidate", PromptStatus.NeedsReview)]
    [InlineData("Draft", PromptStatus.Draft)]
    [InlineData("Deprecated", PromptStatus.NeedsReview)]
    public void MapPromptStatus_DoesNotActivateCandidatePrompts(string status, PromptStatus expected)
        => Assert.Equal(expected, SasdPromptPackageImportService.MapPromptStatus(status));
}
