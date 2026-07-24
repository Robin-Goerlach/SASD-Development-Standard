using TaskHostLocal.Tests.Infrastructure;
using TaskHostLocal.WinForms.Models;
using TaskHostLocal.WinForms.Repositories;

namespace TaskHostLocal.Tests.Repositories;

public sealed class TaskRepositoryTests
{
    [Fact]
    public void GetByListId_EmptyList_ReturnsEmptyResultWithoutSqlError()
    {
        using var database = new TemporaryDatabase();
        var listRepository = new ListRepository(database.ConnectionFactory);
        var taskRepository = new TaskRepository(database.ConnectionFactory);
        var defaultList = Assert.Single(listRepository.GetAll());

        var tasks = taskRepository.GetByListId(defaultList.Id);

        Assert.Empty(tasks);
    }

    [Fact]
    public void AddAndGetByListId_PersistsTask()
    {
        using var database = new TemporaryDatabase();
        var listRepository = new ListRepository(database.ConnectionFactory);
        var taskRepository = new TaskRepository(database.ConnectionFactory);
        var defaultList = Assert.Single(listRepository.GetAll());

        var created = taskRepository.Add(new TaskItem
        {
            ListId = defaultList.Id,
            Title = "SQL-Regression prüfen",
            Description = "Temporäre SQLite-Datenbank",
            DueDate = new DateTime(2026, 7, 31),
            Priority = 2
        });

        var loaded = Assert.Single(taskRepository.GetByListId(defaultList.Id));
        Assert.Equal(created.Id, loaded.Id);
        Assert.Equal("SQL-Regression prüfen", loaded.Title);
        Assert.Equal(new DateTime(2026, 7, 31), loaded.DueDate);
    }

    [Fact]
    public void Search_FindsTitleAndDescriptionAndDoesNotRaiseSqlError()
    {
        using var database = new TemporaryDatabase();
        var listRepository = new ListRepository(database.ConnectionFactory);
        var taskRepository = new TaskRepository(database.ConnectionFactory);
        var defaultList = Assert.Single(listRepository.GetAll());

        taskRepository.Add(new TaskItem
        {
            ListId = defaultList.Id,
            Title = "Build prüfen",
            Description = "Eindeutiges Suchwort Wave01"
        });

        Assert.Single(taskRepository.Search("Build"));
        Assert.Single(taskRepository.Search("Wave01"));
        Assert.Single(taskRepository.Search(string.Empty));
    }

    [Fact]
    public void SetCompleted_TogglesCompletionState()
    {
        using var database = new TemporaryDatabase();
        var listRepository = new ListRepository(database.ConnectionFactory);
        var taskRepository = new TaskRepository(database.ConnectionFactory);
        var defaultList = Assert.Single(listRepository.GetAll());
        var task = taskRepository.Add(new TaskItem
        {
            ListId = defaultList.Id,
            Title = "Abschließen"
        });

        taskRepository.SetCompleted(task.Id, isCompleted: true);
        var completed = Assert.Single(taskRepository.GetByListId(defaultList.Id));
        Assert.True(completed.IsCompleted);
        Assert.NotNull(completed.CompletedAt);

        taskRepository.SetCompleted(task.Id, isCompleted: false);
        var reopened = Assert.Single(taskRepository.GetByListId(defaultList.Id));
        Assert.False(reopened.IsCompleted);
        Assert.Null(reopened.CompletedAt);
    }
}
