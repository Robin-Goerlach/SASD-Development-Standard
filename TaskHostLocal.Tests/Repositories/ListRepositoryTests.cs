using TaskHostLocal.Tests.Infrastructure;
using TaskHostLocal.WinForms.Repositories;

namespace TaskHostLocal.Tests.Repositories;

public sealed class ListRepositoryTests
{
    [Fact]
    public void GetAll_AfterInitialization_ReturnsDefaultList()
    {
        using var database = new TemporaryDatabase();
        var repository = new ListRepository(database.ConnectionFactory);

        var lists = repository.GetAll();

        var defaultList = Assert.Single(lists);
        Assert.Equal("Eingang", defaultList.Name);
    }

    [Fact]
    public void AddAndRename_PersistsListChanges()
    {
        using var database = new TemporaryDatabase();
        var repository = new ListRepository(database.ConnectionFactory);

        var created = repository.Add("Testliste");
        repository.Rename(created.Id, "Umbenannte Liste");

        var renamed = Assert.Single(repository.GetAll(), list => list.Id == created.Id);
        Assert.Equal("Umbenannte Liste", renamed.Name);
    }
}
